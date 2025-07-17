#!/usr/bin/env python3
"""
Test script to verify dashboard template rendering
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, render_template
from user_data import FAKE_ACCOUNTS
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'test-secret-key'

@app.template_filter('aud')
def aud_format(value):
    """Format a number as Australian Dollars"""
    if value < 0:
        return f"-AUD ${abs(value):,.2f}"
    return f"AUD ${value:,.2f}"

def test_dashboard_template():
    """Test dashboard template rendering"""
    try:
        with app.app_context():
            user_data = FAKE_ACCOUNTS['vhamilton']
            current_time = datetime.now().strftime('%I:%M %p')
            
            # Try to render the template
            result = render_template('dashboard.html', user=user_data, current_time=current_time)
            
            print("✅ Dashboard template rendered successfully!")
            print(f"   Template length: {len(result)} characters")
            print(f"   User: {user_data['name']}")
            print(f"   Accounts: {len(user_data['accounts'])}")
            
            return True
    except Exception as e:
        print(f"❌ Template rendering failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_all_users():
    """Test template rendering for all users"""
    all_passed = True
    for username, user_data in FAKE_ACCOUNTS.items():
        try:
            with app.app_context():
                current_time = datetime.now().strftime('%I:%M %p')
                result = render_template('dashboard.html', user=user_data, current_time=current_time)
                print(f"✅ {username} ({user_data['name']}): OK")
        except Exception as e:
            print(f"❌ {username} ({user_data['name']}): FAILED - {e}")
            all_passed = False
    
    return all_passed

if __name__ == '__main__':
    print("Testing dashboard template...")
    print("=" * 50)
    
    # Test main user first
    success = test_dashboard_template()
    
    if success:
        print("\nTesting all users...")
        print("-" * 30)
        all_success = test_all_users()
        
        if all_success:
            print("\n🎉 All tests passed! Dashboard template is working correctly.")
        else:
            print("\n⚠️  Some users failed template rendering.")
    else:
        print("\n💥 Initial test failed. Check template syntax.")
