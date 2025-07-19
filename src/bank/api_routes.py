"""
API routes for the fake bank application
"""
from flask import jsonify, session, request
import random
import time
from .user_data import FAKE_ACCOUNTS

def init_api_routes(app):
    """Initialize API routes"""
    
    @app.route('/api/balance')
    def api_balance():
        if 'user' not in session:
            return jsonify({'error': 'Unauthorized'}), 401
        
        user_data = FAKE_ACCOUNTS[session['user']]
        balances = {}
        for account_type, account in user_data['accounts'].items():
            balances[account_type] = {
                'balance': account['balance'],
                'account_type': account['account_type'],
                'account_number': account['account_number']
            }
            # Add available credit for credit cards
            if 'available_credit' in account:
                balances[account_type]['available_credit'] = account['available_credit']
            # Add available balance for investment accounts
            if 'available_balance' in account:
                balances[account_type]['available_balance'] = account['available_balance']
        
        return jsonify({'accounts': balances})

    @app.route('/api/verify_account', methods=['POST'])
    def verify_account():
        # Fake account verification endpoint
        time.sleep(random.uniform(2, 4))  # Simulate processing
        account_number = request.json.get('account_number', '')
        
        # Always return "valid" for any account number format
        if len(account_number) >= 10:
            return jsonify({'valid': True, 'bank_name': 'Nexus Digital Bank'})
        else:
            return jsonify({'valid': False, 'error': 'Invalid account number format'})

    @app.route('/api/account_info/<account_type>')
    def api_account_info(account_type):
        if 'user' not in session:
            return jsonify({'error': 'Unauthorized'}), 401
        
        user_data = FAKE_ACCOUNTS[session['user']]
        if account_type in user_data['accounts']:
            account = user_data['accounts'][account_type]
            return jsonify({
                'balance': account['balance'],
                'account_type': account['account_type'],
                'account_number': account['account_number'],
                'available_credit': account.get('available_credit', None)
            })
        else:
            return jsonify({'error': 'Account not found'}), 404

    @app.route('/api/resend_2fa', methods=['POST'])
    def api_resend_2fa():
        if 'pending_login' not in session:
            return jsonify({'error': 'No pending login session'}), 400
        
        # Simulate delay
        time.sleep(random.uniform(1, 3))
        
        # Reset timestamp for new code expiry
        session['2fa_timestamp'] = time.time()
        
        return jsonify({
            'success': True, 
            'message': 'New verification code sent'
        })
