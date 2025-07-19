"""
Time-based One-Time Password (TOTP) Manager for Scam Baiting
Generates real verification codes that can be controlled via admin panel
"""
import time
import hmac
import hashlib
import struct
import base64
import random
from datetime import datetime, timedelta

class TOTPManager:
    def __init__(self):
        # Store valid codes per user with expiration times
        self.valid_codes = {}
        # Store generated codes history for admin viewing
        self.code_history = {}
        # Default validity period (30 seconds like real TOTP)
        self.validity_period = 30
        # Secret keys per user (simulated) - using actual system usernames
        self.user_secrets = {
            'vhamilton': 'JBSWY3DPEHPK3PXP',
            'janderson47': 'KRSXG5CTMFRGG5DF', 
            'sbrooks85': 'MNFXK5BAORZXA42A',
            'emartinez48': 'PFXXK4DBPFZXA2BB',
            'achen22': 'KRUGKIDROVUWG2ZA'
        }
    
    def generate_totp(self, secret, timestamp=None):
        """Generate a TOTP code based on secret and current time"""
        if timestamp is None:
            timestamp = int(time.time())
        
        # Convert timestamp to 30-second intervals
        time_step = timestamp // self.validity_period
        
        # Convert secret from base32
        try:
            key = base64.b32decode(secret.upper() + '=' * (-len(secret) % 8))
        except:
            # Fallback to simple hash if base32 fails
            key = secret.encode('utf-8')
        
        # Create HMAC-SHA1
        time_bytes = struct.pack('>Q', time_step)
        hmac_hash = hmac.new(key, time_bytes, hashlib.sha1).digest()
        
        # Dynamic truncation
        offset = hmac_hash[-1] & 0x0f
        truncated_hash = hmac_hash[offset:offset+4]
        code = struct.unpack('>I', truncated_hash)[0]
        code = code & 0x7fffffff
        code = code % 1000000
        
        return f"{code:06d}"
    
    def generate_valid_code_for_user(self, username):
        """Generate a new valid code for a specific user"""
        if username not in self.user_secrets:
            # Generate random 6-digit code for unknown users
            code = f"{random.randint(0, 999999):06d}"
        else:
            # Generate real TOTP code
            secret = self.user_secrets[username]
            code = self.generate_totp(secret)
        
        # Store with expiration time
        expiry_time = time.time() + self.validity_period
        
        if username not in self.valid_codes:
            self.valid_codes[username] = []
        
        # Add new code
        self.valid_codes[username].append({
            'code': code,
            'generated_at': time.time(),
            'expires_at': expiry_time,
            'used': False
        })
        
        # Store in history for admin viewing
        if username not in self.code_history:
            self.code_history[username] = []
        
        self.code_history[username].append({
            'code': code,
            'generated_at': datetime.now(),
            'expires_at': datetime.fromtimestamp(expiry_time),
            'method': self.get_user_2fa_method(username),
            'status': 'active'
        })
        
        # Clean up expired codes
        self.cleanup_expired_codes(username)
        
        return code
    
    def is_valid_code(self, username, code):
        """Check if a code is valid for the given user"""
        if username not in self.valid_codes:
            return False
        
        current_time = time.time()
        
        for code_info in self.valid_codes[username]:
            if (code_info['code'] == code and 
                not code_info['used'] and 
                current_time <= code_info['expires_at']):
                
                # Mark as used
                code_info['used'] = True
                
                # Update history
                for hist_code in self.code_history[username]:
                    if hist_code['code'] == code:
                        hist_code['status'] = 'used'
                        break
                
                return True
        
        return False
    
    def cleanup_expired_codes(self, username):
        """Remove expired codes for a user"""
        if username not in self.valid_codes:
            return
        
        current_time = time.time()
        
        # Remove expired codes from valid_codes
        self.valid_codes[username] = [
            code_info for code_info in self.valid_codes[username]
            if current_time <= code_info['expires_at']
        ]
        
        # Update history status for expired codes
        for hist_code in self.code_history[username]:
            if (hist_code['status'] == 'active' and 
                datetime.now() > hist_code['expires_at']):
                hist_code['status'] = 'expired'
    
    def get_user_2fa_method(self, username):
        """Get the 2FA method for a user (for display purposes)"""
        methods = {
            'vhamilton': 'Authenticator App',
            'janderson47': 'SMS to +61 4** *** 123',
            'sbrooks85': 'Email to s****@email.com',
            'emartinez48': 'SMS to +61 4** *** 789',
            'achen22': 'Email to a****@email.com'
        }
        return methods.get(username, 'SMS to registered phone')
    
    def get_active_codes_for_user(self, username):
        """Get all active codes for a user (for admin viewing)"""
        if username not in self.code_history:
            return []
        
        # Cleanup first
        self.cleanup_expired_codes(username)
        
        return [
            code_info for code_info in self.code_history[username]
            if code_info['status'] == 'active'
        ]
    
    def get_all_user_codes(self):
        """Get active codes for all users (for admin dashboard)"""
        all_codes = {}
        
        for username in self.user_secrets.keys():
            all_codes[username] = self.get_active_codes_for_user(username)
        
        return all_codes
    
    def generate_codes_for_all_users(self):
        """Generate new codes for all users (admin function)"""
        generated = {}
        
        for username in self.user_secrets.keys():
            code = self.generate_valid_code_for_user(username)
            generated[username] = code
        
        return generated
    
    def force_expire_all_codes(self):
        """Force expire all active codes (emergency admin function)"""
        for username in self.valid_codes:
            for code_info in self.valid_codes[username]:
                code_info['expires_at'] = time.time() - 1
            
        for username in self.code_history:
            for hist_code in self.code_history[username]:
                if hist_code['status'] == 'active':
                    hist_code['status'] = 'force_expired'
    
    def get_code_stats(self):
        """Get statistics for admin dashboard"""
        stats = {
            'total_users': len(self.user_secrets),
            'users_with_active_codes': 0,
            'total_active_codes': 0,
            'total_generated_today': 0
        }
        
        today = datetime.now().date()
        
        for username in self.user_secrets.keys():
            active_codes = self.get_active_codes_for_user(username)
            if active_codes:
                stats['users_with_active_codes'] += 1
                stats['total_active_codes'] += len(active_codes)
            
            # Count today's generated codes
            if username in self.code_history:
                today_codes = [
                    code for code in self.code_history[username]
                    if code['generated_at'].date() == today
                ]
                stats['total_generated_today'] += len(today_codes)
        
        return stats

# Global instance
totp_manager = TOTPManager()
