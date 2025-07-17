"""
Configuration settings for the fake bank application
"""
import secrets

# Flask configuration
SECRET_KEY = secrets.token_hex(16)
DEBUG = True
PORT = 5000

# Security settings
BLACKLISTED_2FA_CODES = [
    '000000', '111111', '222222', '333333', '444444',
    '555555', '666666', '777777', '888888', '999999'
]

# Lockout settings
LOCKOUT_DURATION = 15 * 60  # 15 minutes in seconds
MAX_2FA_ATTEMPTS = 3
MAX_BLACKLIST_ATTEMPTS = 3
SESSION_2FA_TIMEOUT = 300  # 5 minutes

# Processing delay settings
MIN_DELAY = 0.5
MAX_DELAY = 2.0
