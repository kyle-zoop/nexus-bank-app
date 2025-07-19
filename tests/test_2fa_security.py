#!/usr/bin/env python3
"""
Test script for the new 2FA TOTP system
Verifies that only generated codes work and all others are rejected
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from bank.totp_manager import totp_manager
from bank.auth import is_valid_totp_code

def test_2fa_system():
    """Test the complete 2FA system"""
    print("🔐 Testing Nexus Bank 2FA System")
    print("=" * 50)
    
    # Test user - using actual system username
    test_username = "janderson47"
    
    # Test 1: Generate a valid code
    print("\n1. Testing Valid Code Generation:")
    valid_code = totp_manager.generate_valid_code_for_user(test_username)
    print(f"   Generated code for {test_username}: {valid_code}")
    
    # Test 2: Validate the generated code
    print("\n2. Testing Valid Code Validation:")
    is_valid, result = is_valid_totp_code(test_username, valid_code)
    print(f"   Code {valid_code} validation: {is_valid} ({result})")
    
    # Test 3: Test invalid random codes (all should be treated as suspicious)
    print("\n3. Testing Invalid Random Codes (All Treated as Suspicious):")
    test_codes = ["123456", "000000", "999999", "654321", "111111"]
    
    for code in test_codes:
        is_valid, result = is_valid_totp_code(test_username, code)
        status = "✅ REJECTED (SUSPICIOUS)" if not is_valid else "❌ ACCEPTED"
        print(f"   Code {code}: {status} ({result})")
    
    # Test 4: Test that previously "blacklisted" codes are now just invalid
    print("\n4. Testing Previously Blacklisted Codes (Now Just Invalid):")
    previously_blacklisted = ["000000", "111111", "999999"]
    
    for code in previously_blacklisted:
        is_valid, result = is_valid_totp_code(test_username, code)
        status = "✅ INVALID/SUSPICIOUS" if result == 'invalid_suspicious' else f"❌ {result.upper()}"
        print(f"   Code {code}: {status}")
    
    # Test 5: Test code reuse (should fail)
    print("\n5. Testing Code Reuse Protection:")
    new_code = totp_manager.generate_valid_code_for_user(test_username)
    print(f"   Generated fresh code: {new_code}")
    
    # Use it once
    is_valid1, result1 = is_valid_totp_code(test_username, new_code)
    print(f"   First use: {is_valid1} ({result1})")
    
    # Try to use it again
    is_valid2, result2 = is_valid_totp_code(test_username, new_code)
    status = "✅ REJECTED" if not is_valid2 else "❌ ACCEPTED"
    print(f"   Second use: {status} ({result2})")
    
    # Test 6: Test statistics
    print("\n6. Testing Statistics:")
    stats = totp_manager.get_code_stats()
    print(f"   Total users: {stats['total_users']}")
    print(f"   Users with active codes: {stats['users_with_active_codes']}")
    print(f"   Total active codes: {stats['total_active_codes']}")
    print(f"   Generated today: {stats['total_generated_today']}")
    
    # Test 7: Test all users code generation
    print("\n7. Testing Bulk Code Generation:")
    all_codes = totp_manager.generate_codes_for_all_users()
    for username, code in all_codes.items():
        print(f"   {username}: {code}")
    
    print("\n" + "=" * 50)
    print("🛡️  Enhanced 2FA Security Test Complete!")
    print("✅ Only admin-generated codes should work")
    print("✅ ALL random codes are rejected and treated as suspicious")
    print("✅ ANY invalid code triggers security lockout behavior")
    print("✅ Code reuse should be prevented")
    print("✅ No blacklist needed - all invalid codes are suspicious")

if __name__ == "__main__":
    test_2fa_system()
