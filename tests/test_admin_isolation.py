#!/usr/bin/env python3
"""
Test script to verify that admin messages don't leak to regular users
"""
import requests
import sys

def test_no_admin_leaks():
    """Test that admin messages don't appear in regular login flow"""
    print("🔐 Testing Admin Message Isolation")
    print("=" * 50)
    
    base_url = "http://127.0.0.1:5000"
    
    # Create a session (simulating a regular user)
    session = requests.Session()
    
    try:
        # Step 1: Get login page
        print("\n1. Accessing login page...")
        response = session.get(f"{base_url}/login")
        if response.status_code != 200:
            print(f"❌ Failed to access login page: {response.status_code}")
            return False
        print("✅ Login page accessible")
        
        # Step 2: Submit valid credentials (this should trigger 2FA code generation)
        print("\n2. Submitting valid credentials...")
        login_data = {
            'username': 'janderson47',
            'password': 'JohnA@2024'
        }
        response = session.post(f"{base_url}/login", data=login_data)
        
        # Check if response contains any admin messages
        response_text = response.text.lower()
        
        print(f"Response status: {response.status_code}")
        
        # Look for admin indicators that shouldn't be there
        admin_indicators = [
            '[admin]',
            'generated 2fa code',
            'admin generated',
            'admin:'
        ]
        
        found_admin_content = []
        for indicator in admin_indicators:
            if indicator in response_text:
                found_admin_content.append(indicator)
        
        if found_admin_content:
            print(f"❌ Admin content leaked to user: {found_admin_content}")
            return False
        else:
            print("✅ No admin content found in user response")
        
        # Step 3: Check that 2FA prompt is shown (but without admin info)
        if '2fa' in response_text or 'two-factor' in response_text or 'verification' in response_text:
            print("✅ 2FA prompt shown to user (as expected)")
        else:
            print("❓ 2FA prompt might not be showing (check manually)")
        
        print("\n" + "=" * 50)
        print("🛡️ Admin Isolation Test Complete!")
        print("✅ No admin messages leaked to regular users")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        print("💡 Make sure the application is running on port 5000")
        return False

if __name__ == "__main__":
    success = test_no_admin_leaks()
    sys.exit(0 if success else 1)
