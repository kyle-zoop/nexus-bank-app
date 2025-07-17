#!/usr/bin/env python3
"""
Test script to verify statements template rendering
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

def test_statements_template():
    """Test statements template rendering"""
    try:
        with app.app_context():
            user_data = FAKE_ACCOUNTS['vhamilton']
            
            # Try to render the template
            result = render_template('statements.html', user=user_data)
            
            print("✅ Statements template rendered successfully!")
            print(f"   Template length: {len(result)} characters")
            print(f"   User: {user_data['name']}")
            print(f"   Accounts: {len(user_data['accounts'])}")
            
            return True
    except Exception as e:
        print(f"❌ Template rendering failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    print("Testing statements template...")
    print("=" * 40)
    
    success = test_statements_template()
    
    if success:
        print("\n🎉 Statements template is working correctly!")
    else:
        print("\n💥 Template test failed. Check template syntax.")
