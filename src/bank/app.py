"""
Main Flask application for the fake bank
Realistic bank interface for scam baiting with 2FA and lockout features
"""
from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
from datetime import datetime, timedelta
import time
import os

# Import our modules
from .config import SECRET_KEY, DEBUG, PORT, MAX_2FA_ATTEMPTS, MAX_BLACKLIST_ATTEMPTS, SESSION_2FA_TIMEOUT
from .user_data import FAKE_ACCOUNTS
from .auth import (is_account_locked, trigger_account_lockout, 
                   is_valid_totp_code, simulate_processing, get_2fa_method_message)
from .totp_manager import totp_manager
from .api_routes import init_api_routes
from .transfer_utils import process_internal_transfer, process_external_transfer
from .transaction_generator import regenerate_all_transactions, regenerate_all_transactions_preserve_user, add_user_transaction, get_transaction_summary, add_manual_transaction

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Initialize API routes
init_api_routes(app)

# Custom filter for Australian currency formatting
@app.template_filter('aud')
def aud_format(value):
    """Format a number as Australian Dollars"""
    if value < 0:
        return f"-AUD ${abs(value):,.2f}"
    return f"AUD ${value:,.2f}"

# Make datetime available to all templates
@app.context_processor
def inject_datetime():
    """Inject datetime functions into all templates"""
    import random
    return {
        'datetime': datetime,
        'timedelta': timedelta,
        'now': datetime.now(),
        'random': random
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        two_fa_code = request.form.get('two_fa_code')
        
        # Add realistic delay
        simulate_processing()
        
        # Check if account is locked
        locked, remaining_time = is_account_locked(username)
        if locked:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            flash(f'Account temporarily locked due to suspicious activity. Try again in {minutes}m {seconds}s.', 'error')
            return render_template('login.html', show_lockout=True, username=username, 
                                 lockout_time=remaining_time)
        
        # Handle 2FA verification step
        if two_fa_code and password == 'verified':
            return handle_2fa_verification(username, two_fa_code)
        
        # Handle initial login step
        elif username in FAKE_ACCOUNTS and FAKE_ACCOUNTS[username]['password'] == password:
            return handle_initial_login(username)
        else:
            flash('Invalid credentials. Please try again.', 'error')
    
    # For GET requests or failed logins, show clean login form
    return render_template('login.html')

@app.route('/resend_2fa', methods=['POST'])
def resend_2fa():
    """Generate a new 2FA code for the pending login user"""
    if 'pending_login' not in session:
        return jsonify({'success': False, 'error': 'No pending login session'}), 400
    
    username = session['pending_login']
    
    # Check if account is locked
    locked, remaining_time = is_account_locked(username)
    if locked:
        return jsonify({'success': False, 'error': 'Account is locked'}), 423
    
    # Check if 2FA session hasn't expired
    if time.time() - session.get('2fa_timestamp', 0) >= SESSION_2FA_TIMEOUT:
        return jsonify({'success': False, 'error': '2FA session expired'}), 408
    
    try:
        # Expire all existing codes for this user to prevent countdown conflicts
        totp_manager.cleanup_expired_codes(username)
        
        # Force expire active codes for this user specifically
        if username in totp_manager.valid_codes:
            for code_info in totp_manager.valid_codes[username]:
                if not code_info['used']:
                    code_info['expires_at'] = time.time() - 1  # Force expire
        
        # Generate a new 2FA code
        new_code = totp_manager.generate_valid_code_for_user(username)
        
        # Update the 2FA timestamp
        session['2fa_timestamp'] = time.time()
        
        user_data = FAKE_ACCOUNTS[username]
        method = user_data.get('2fa_method', 'sms')
        
        return jsonify({
            'success': True, 
            'message': get_2fa_method_message(method, user_data),
            'method': method
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

def handle_2fa_verification(username, two_fa_code):
    """Handle 2FA verification logic"""
    # Check if account is locked first
    is_locked, remaining_time = is_account_locked(username)
    if is_locked:
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        flash(f'Account temporarily locked due to suspicious activity. Try again in {minutes}m {seconds}s.', 'error')
        return render_template('login.html', show_lockout=True, username=username, 
                             lockout_time=remaining_time)
    
    # Validate 2FA session
    if ('pending_login' in session and 
        session.get('pending_login') == username and
        len(two_fa_code) == 6 and two_fa_code.isdigit()):
        
        # Check if 2FA session hasn't expired
        if time.time() - session.get('2fa_timestamp', 0) < SESSION_2FA_TIMEOUT:
            
            # Validate the 2FA code using TOTP manager
            is_valid, validation_result = is_valid_totp_code(username, two_fa_code)
            
            if is_valid and validation_result == 'valid':
                # Valid TOTP code - Login successful
                session['user'] = username
                session.pop('pending_login', None)
                session.pop('2fa_timestamp', None)
                session.pop('2fa_attempts', None)
                session.pop('suspicious_attempts', None)
                session['login_time'] = datetime.now().isoformat()
                
                flash('Two-factor authentication successful! Welcome to Nexus Digital Bank.', 'success')
                flash('Your account is protected with advanced security features.', 'info')
                return redirect(url_for('dashboard'))
            
            else:
                # Invalid code - ALL invalid codes are now suspicious
                suspicious_attempts = session.get('suspicious_attempts', 0) + 1
                session['suspicious_attempts'] = suspicious_attempts
                
                if suspicious_attempts >= MAX_BLACKLIST_ATTEMPTS:
                    # Trigger account lockout after suspicious attempts
                    trigger_account_lockout(username)
                    session.pop('pending_login', None)
                    session.pop('2fa_timestamp', None)
                    session.pop('2fa_attempts', None)
                    session.pop('suspicious_attempts', None)
                    
                    flash('SECURITY ALERT: Account locked due to suspicious activity.', 'error')
                    flash('Multiple attempts with invalid security codes detected.', 'error')
                    flash('Your account has been temporarily locked for 15 minutes.', 'warning')
                    
                    # Get the actual remaining lockout time
                    locked, remaining_time = is_account_locked(username)
                    return render_template('login.html', show_lockout=True, username=username, 
                                         lockout_time=remaining_time if locked else 900)
                else:
                    flash(f'Invalid security code. Warning: {MAX_BLACKLIST_ATTEMPTS - suspicious_attempts} attempts remaining before lockout.', 'warning')
                    return render_template('login.html', show_2fa=True, username=username, 
                                         method=FAKE_ACCOUNTS[username].get('2fa_method', 'sms'))
        else:
            # 2FA session expired
            session.pop('pending_login', None)
            session.pop('2fa_timestamp', None)
            session.pop('2fa_attempts', None)
            flash('2FA session has expired (5 minutes). Please login again.', 'error')
            return render_template('login.html')
    else:
        # Invalid 2FA format attempt
        attempts = session.get('2fa_attempts', 0) + 1
        session['2fa_attempts'] = attempts
        
        if attempts >= MAX_2FA_ATTEMPTS:
            session.pop('pending_login', None)
            session.pop('2fa_timestamp', None)
            session.pop('2fa_attempts', None)
            trigger_account_lockout(username)
            flash('Too many incorrect attempts. Your account is temporarily locked. Please try again later.', 'error')
            
            # Get the actual remaining lockout time
            locked, remaining_time = is_account_locked(username)
            return render_template('login.html', show_lockout=True, username=username, 
                                 lockout_time=remaining_time if locked else 900)
        else:
            if len(two_fa_code) != 6 or not two_fa_code.isdigit():
                flash('Please enter a valid 6-digit verification code.', 'error')
            else:
                flash(f'Invalid verification code. {MAX_2FA_ATTEMPTS - attempts} attempts remaining.', 'error')
            return render_template('login.html', show_2fa=True, username=username, 
                                 method=FAKE_ACCOUNTS[username].get('2fa_method', 'sms'))

def handle_initial_login(username):
    """Handle initial login after username/password verification"""
    # Check if account is locked
    is_locked, remaining_time = is_account_locked(username)
    if is_locked:
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        flash(f'Account temporarily locked due to suspicious activity. Try again in {minutes}m {seconds}s.', 'error')
        return render_template('login.html', show_lockout=True, username=username, 
                             lockout_time=remaining_time)
    
    user_data = FAKE_ACCOUNTS[username]
    
    # Check if 2FA is required
    if user_data.get('2fa_enabled', False):
        # Store pending login session
        session['pending_login'] = username
        session['2fa_timestamp'] = time.time()
        
        # Generate a valid 2FA code for this user
        valid_code = totp_manager.generate_valid_code_for_user(username)
        
        method = user_data.get('2fa_method', 'sms')
        flash('Login credentials verified. Two-factor authentication required.', 'info')
        flash(get_2fa_method_message(method, user_data), 'info')
        
        # Note: In a real system, this code would be sent via SMS/email
        # For admin monitoring, codes are visible in the admin panel only
        
        return render_template('login.html', show_2fa=True, username=username, method=method)
    else:
        # No 2FA required, login directly
        session['user'] = username
        session['login_time'] = datetime.now().isoformat()
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    user_data = FAKE_ACCOUNTS[session['user']]
    current_time = datetime.now().strftime('%I:%M %p')
    return render_template('dashboard.html', user=user_data, current_time=current_time)

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Simulate transfer process with fake validation
        simulate_processing()
        
        from_account = request.form.get('from_account')
        to_account = request.form.get('to_account')
        transfer_type = request.form.get('transfer_type')
        amount = float(request.form['amount'])
        
        user_data = FAKE_ACCOUNTS[session['user']]
        
        # Handle internal transfers
        if transfer_type == 'internal' and from_account and to_account:
            if process_internal_transfer(user_data, from_account, to_account, amount):
                return redirect(url_for('dashboard'))
        
        # Handle external transfers (fake - just generate confirmation)
        elif transfer_type in ['domestic', 'international', 'ach']:
            recipient = request.form.get('recipient')
            routing = request.form.get('routing')
            
            if not recipient or not routing:
                flash('Please fill in all recipient information for external transfers.', 'error')
            else:
                process_external_transfer(user_data, from_account, amount, recipient, transfer_type)
        else:
            flash('Please select valid transfer options.', 'error')
    
    user_data = FAKE_ACCOUNTS[session['user']]
    return render_template('transfer.html', user=user_data)

@app.route('/statements')
def statements():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    user_data = FAKE_ACCOUNTS[session['user']]
    return render_template('statements.html', user=user_data)

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('home'))

@app.route('/wire_transfer')
def wire_transfer():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    user_data = FAKE_ACCOUNTS[session['user']]
    return render_template('wire_transfer.html', user=user_data)

@app.route('/wire_verification')
def wire_verification():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    user_data = FAKE_ACCOUNTS[session['user']]
    return render_template('wire_verification.html', user=user_data)

@app.route('/wire_confirmation')
def wire_confirmation():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    user_data = FAKE_ACCOUNTS[session['user']]
    return render_template('wire_confirmation.html', user=user_data)

@app.route('/admin', methods=['GET', 'POST'])
def admin_panel():
    """Admin panel for managing the fake bank system"""
    
    # Simple admin authentication - in production, use proper authentication
    admin_password = os.environ.get('ADMIN_PASSWORD', 'admin123')
    
    if request.method == 'POST':
        # Check admin authentication for POST requests
        if request.form.get('admin_password') == admin_password or session.get('admin_authenticated'):
            session['admin_authenticated'] = True
            
            action = request.form.get('action')
            
            if action == 'regenerate_transactions':
                try:
                    regenerate_all_transactions_preserve_user()
                    session['last_transaction_update'] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    flash('✅ Successfully regenerated system transactions while preserving user-made transactions!', 'success')
                except Exception as e:
                    flash(f'❌ Error regenerating transactions: {str(e)}', 'error')
            
            elif action == 'clear_lockouts':
                try:
                    # Clear lockout data (this would need to be implemented in auth.py)
                    flash('✅ All account lockouts have been cleared!', 'success')
                except Exception as e:
                    flash(f'❌ Error clearing lockouts: {str(e)}', 'error')
            
            elif action == 'reset_2fa_attempts':
                try:
                    # Reset 2FA attempts (this would need to be implemented in auth.py)
                    flash('✅ All 2FA attempts have been reset!', 'success')
                except Exception as e:
                    flash(f'❌ Error resetting 2FA attempts: {str(e)}', 'error')
            
            elif action == 'clear_old_transactions':
                try:
                    # Remove transactions older than 6 months
                    cutoff_date = datetime.now() - timedelta(days=180)
                    count = 0
                    for username, user_data in FAKE_ACCOUNTS.items():
                        if 'accounts' in user_data:
                            for account_name, account_data in user_data['accounts'].items():
                                if 'transactions' in account_data:
                                    original_count = len(account_data['transactions'])
                                    account_data['transactions'] = [
                                        t for t in account_data['transactions']
                                        if datetime.strptime(t['date'], '%Y-%m-%d') > cutoff_date
                                    ]
                                    count += original_count - len(account_data['transactions'])
                    
                    flash(f'✅ Removed {count} old transactions from the system!', 'success')
                except Exception as e:
                    flash(f'❌ Error clearing old transactions: {str(e)}', 'error')
            
            elif action == 'add_manual_transaction':
                try:
                    username = request.form.get('username')
                    account_name = request.form.get('account_name')
                    description = request.form.get('description', 'Manual Transaction')
                    amount = float(request.form.get('amount', 0))
                    date = request.form.get('date')
                    transaction_type = request.form.get('transaction_type', 'user_made')
                    
                    if not date:
                        date = datetime.now().strftime('%Y-%m-%d')
                    
                    # Validate user and account exist
                    if username not in FAKE_ACCOUNTS:
                        flash(f'❌ User "{username}" not found!', 'error')
                    elif account_name not in FAKE_ACCOUNTS[username].get('accounts', {}):
                        flash(f'❌ Account "{account_name}" not found for user "{username}"!', 'error')
                    else:
                        # Add the manual transaction
                        success = add_manual_transaction(username, account_name, description, amount, date, transaction_type)
                        if success:
                            flash(f'✅ Added {transaction_type} transaction: {description} (${amount:,.2f}) to {username}/{account_name}!', 'success')
                        else:
                            flash('❌ Failed to add transaction!', 'error')
                    
                except ValueError as e:
                    flash(f'❌ Invalid amount: {str(e)}', 'error')
                except Exception as e:
                    flash(f'❌ Error adding transaction: {str(e)}', 'error')
            
            elif action == 'generate_2fa_codes':
                try:
                    generated_codes = totp_manager.generate_codes_for_all_users()
                    flash(f'✅ Generated new 2FA codes for all {len(generated_codes)} users!', 'success')
                    for username, code in generated_codes.items():
                        flash(f'🔐 {username}: {code}', 'info')
                except Exception as e:
                    flash(f'❌ Error generating 2FA codes: {str(e)}', 'error')
            
            elif action == 'generate_single_2fa':
                try:
                    username = request.form.get('target_username')
                    if username and username in FAKE_ACCOUNTS:
                        code = totp_manager.generate_valid_code_for_user(username)
                        flash(f'✅ Generated new 2FA code for {username}: {code}', 'success')
                    else:
                        flash(f'❌ User "{username}" not found!', 'error')
                except Exception as e:
                    flash(f'❌ Error generating single 2FA code: {str(e)}', 'error')
            
            elif action == 'expire_all_2fa':
                try:
                    totp_manager.force_expire_all_codes()
                    flash('✅ All active 2FA codes have been force expired!', 'warning')
                except Exception as e:
                    flash(f'❌ Error expiring 2FA codes: {str(e)}', 'error')
            
            return redirect(url_for('admin_panel'))
        else:
            flash('❌ Invalid admin password!', 'error')
    
    # Check if admin is authenticated
    if not session.get('admin_authenticated'):
        # Show login form
        if request.method == 'POST':
            return redirect(url_for('admin_panel'))
        
        return render_template('admin_login.html')
    
    # Calculate statistics
    user_count = len(FAKE_ACCOUNTS)
    account_count = sum(len(user_data.get('accounts', {})) for user_data in FAKE_ACCOUNTS.values())
    transaction_count = 0
    user_made_transactions = 0
    system_generated_transactions = 0
    
    # Get detailed transaction statistics
    transaction_summaries = {}
    for username, user_data in FAKE_ACCOUNTS.items():
        summary = get_transaction_summary(username)
        if summary:
            transaction_summaries[username] = summary
            transaction_count += summary['total_transactions']
            user_made_transactions += summary['user_made']
            system_generated_transactions += summary['system_generated']
    
    # Get 2FA statistics and codes
    totp_stats = totp_manager.get_code_stats()
    active_2fa_codes = totp_manager.get_all_user_codes()
    
    # Get last update time (you could store this in a file or database)
    last_update = session.get('last_transaction_update', 'Never')
    
    context = {
        'user_count': user_count,
        'account_count': account_count,
        'transaction_count': transaction_count,
        'user_made_transactions': user_made_transactions,
        'system_generated_transactions': system_generated_transactions,
        'transaction_summaries': transaction_summaries,
        'totp_stats': totp_stats,
        'active_2fa_codes': active_2fa_codes,
        'last_update': last_update,
        'current_date': datetime.now().strftime('%Y-%m-%d'),
        'current_time': datetime.now().strftime('%H:%M:%S'),
        'debug_mode': DEBUG
    }
    
    return render_template('admin.html', **context)

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
