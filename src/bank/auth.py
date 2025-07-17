"""
Security and authentication utilities for the fake bank application
"""
import time
import random
from .config import LOCKOUT_DURATION, BLACKLISTED_2FA_CODES, MIN_DELAY, MAX_DELAY

# Account lockout tracking
ACCOUNT_LOCKOUTS = {}

def is_account_locked(username):
    """Check if account is currently locked out"""
    if username not in ACCOUNT_LOCKOUTS:
        return False, 0
    
    lockout_data = ACCOUNT_LOCKOUTS[username]
    lockout_until = lockout_data.get('locked_until', 0)
    current_time = time.time()
    
    if current_time < lockout_until:
        remaining_time = int(lockout_until - current_time)
        return True, remaining_time
    else:
        # Lockout expired, remove it
        del ACCOUNT_LOCKOUTS[username]
        return False, 0

def trigger_account_lockout(username):
    """Lock account for 15 minutes after 3 blacklisted code attempts"""
    ACCOUNT_LOCKOUTS[username] = {
        'locked_until': time.time() + LOCKOUT_DURATION,
        'reason': 'Suspicious activity detected - Multiple invalid security codes'
    }

def is_blacklisted_code(code):
    """Check if a 2FA code is blacklisted"""
    return code in BLACKLISTED_2FA_CODES

def simulate_processing():
    """Simulate realistic processing delays"""
    time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))

def get_2fa_method_message(method, user_data):
    """Get appropriate 2FA message based on method"""
    method_messages = {
        'sms': f'SMS verification code sent to {user_data.get("2fa_phone", "your registered phone")}',
        'email': f'Email verification code sent to {user_data.get("email", "your registered email")}',
        'app': 'Please check your authenticator app for the verification code'
    }
    return method_messages.get(method, 'Verification code sent to your registered device.')

def clear_lockouts():
    """Clear all account lockouts (useful for testing)"""
    global ACCOUNT_LOCKOUTS
    ACCOUNT_LOCKOUTS.clear()
