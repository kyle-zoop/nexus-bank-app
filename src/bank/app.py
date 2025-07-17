"""
Main Flask application for the fake bank
Realistic bank interface for scam baiting with 2FA and lockout features
"""
from flask import Flask, render_template, request, session, redirect, url_for, flash
from datetime import datetime
import time

# Import our modules
from .config import SECRET_KEY, DEBUG, PORT, MAX_2FA_ATTEMPTS, MAX_BLACKLIST_ATTEMPTS, SESSION_2FA_TIMEOUT
from .user_data import FAKE_ACCOUNTS
from .auth import (is_account_locked, trigger_account_lockout, is_blacklisted_code, 
                   simulate_processing, get_2fa_method_message)
from .api_routes import init_api_routes
from .transfer_utils import process_internal_transfer, process_external_transfer

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
            
            # Check if code is blacklisted
            if is_blacklisted_code(two_fa_code):
                blacklist_attempts = session.get('blacklist_attempts', 0) + 1
                session['blacklist_attempts'] = blacklist_attempts
                
                if blacklist_attempts >= MAX_BLACKLIST_ATTEMPTS:
                    # Trigger account lockout
                    trigger_account_lockout(username)
                    session.pop('pending_login', None)
                    session.pop('2fa_timestamp', None)
                    session.pop('2fa_attempts', None)
                    session.pop('blacklist_attempts', None)
                    
                    flash('SECURITY ALERT: Account locked due to suspicious activity.', 'error')
                    flash('Multiple attempts with invalid security codes detected.', 'error')
                    flash('Your account has been temporarily locked for 15 minutes.', 'warning')
                    
                    return render_template('login.html', show_lockout=True, username=username, 
                                         lockout_time=15*60)
                else:
                    flash(f'Invalid security code. Warning: {MAX_BLACKLIST_ATTEMPTS - blacklist_attempts} attempts remaining before lockout.', 'warning')
                    return render_template('login.html', show_2fa=True, username=username, 
                                         method=FAKE_ACCOUNTS[username].get('2fa_method', 'sms'))
            
            # Valid code (not blacklisted) - Login successful
            session['user'] = username
            session.pop('pending_login', None)
            session.pop('2fa_timestamp', None)
            session.pop('2fa_attempts', None)
            session.pop('blacklist_attempts', None)
            session['login_time'] = datetime.now().isoformat()
            
            flash('Two-factor authentication successful! Welcome to Nexus Digital Bank.', 'success')
            flash('Your account is protected with advanced security features.', 'info')
            return redirect(url_for('dashboard'))
        else:
            # 2FA session expired
            session.pop('pending_login', None)
            session.pop('2fa_timestamp', None)
            session.pop('2fa_attempts', None)
            flash('2FA session has expired (5 minutes). Please login again.', 'error')
            return render_template('login.html')
    else:
        # Invalid 2FA attempt
        attempts = session.get('2fa_attempts', 0) + 1
        session['2fa_attempts'] = attempts
        
        if attempts >= MAX_2FA_ATTEMPTS:
            session.pop('pending_login', None)
            session.pop('2fa_timestamp', None)
            session.pop('2fa_attempts', None)
            trigger_account_lockout(username)
            flash('Too many incorrect attempts. Your account is temporarily locked. Please try again later.', 'error')
            return render_template('login.html')
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
        
        method = user_data.get('2fa_method', 'sms')
        flash('Login credentials verified. Two-factor authentication required.', 'info')
        flash(get_2fa_method_message(method, user_data), 'info')
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

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
