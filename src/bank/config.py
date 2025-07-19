"""
Configuration settings for the fake bank application
"""
import secrets
import os

# Flask configuration
SECRET_KEY = os.environ.get('SECRET_KEY', secrets.token_hex(16))
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
PORT = int(os.environ.get('PORT', 5000))

# Security settings - Enhanced for scam baiting
# All invalid 2FA codes now trigger suspicious activity detection

# Lockout settings
LOCKOUT_DURATION = 15 * 60  # 15 minutes in seconds
MAX_2FA_ATTEMPTS = 3
MAX_BLACKLIST_ATTEMPTS = 3  # Now used for any invalid code attempts
SESSION_2FA_TIMEOUT = 300  # 5 minutes

# Processing delay settings
MIN_DELAY = 0.5
MAX_DELAY = 2.0
