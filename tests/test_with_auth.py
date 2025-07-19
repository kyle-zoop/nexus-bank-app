#!/usr/bin/env python3
"""
Test with authentication to verify moment.js fix
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from bank.app import app

def test_with_auth():
    """Test templates with proper authentication"""
    print("Testing with authentication...")
    
    with app.test_client() as client:
        try:
            # First, log in
            print("  Logging in...")
            response = client.post('/login', data={
                'username': 'janderson47',
                'password': 'Password123!'
            }, follow_redirects=True)
            
            if response.status_code != 200:
                print(f"    ❌ Login failed with status: {response.status_code}")
                return False
                
            print("    ✅ Logged in successfully")
            
            # Test wire verification page
            print("  Testing wire verification page...")
            response = client.get('/wire_verification?amount=5000.00&recipient_name=Test&bank_name=TestBank&bank_country=Australia&purpose=Test')
            
            if response.status_code == 200:
                print("    ✅ Wire verification page loads successfully")
                html_content = response.data.decode('utf-8')
                if 'moment()' not in html_content:
                    print("    ✅ No moment() references found")
                else:
                    print("    ❌ Still contains moment() references")
                    return False
                    
                if 'WTR-' in html_content:
                    print("    ✅ Reference number generated correctly")
                else:
                    print("    ❌ Reference number not found")
                    
            else:
                print(f"    ❌ Failed with status: {response.status_code}")
                return False
                
            # Test wire confirmation page  
            print("  Testing wire confirmation page...")
            response = client.get('/wire_confirmation?amount=5000.00&recipient_name=Test&bank_name=TestBank')
            
            if response.status_code == 200:
                print("    ✅ Wire confirmation page loads successfully")
                html_content = response.data.decode('utf-8')
                if 'moment()' not in html_content:
                    print("    ✅ No moment() references found")
                else:
                    print("    ❌ Still contains moment() references")
                    return False
                    
                if 'WTR-' in html_content:
                    print("    ✅ Reference number generated correctly")
                else:
                    print("    ❌ Reference number not found")
                    
            else:
                print(f"    ❌ Failed with status: {response.status_code}")
                return False
                
            return True
            
        except Exception as e:
            print(f"    ❌ Error: {e}")
            import traceback
            traceback.print_exc()
            return False

if __name__ == "__main__":
    print("=" * 60)
    
    if test_with_auth():
        print("=" * 60)
        print("🎉 SUCCESS: Wire pages work correctly without moment.js errors!")
        print("✅ The UndefinedError: 'moment' is undefined issue has been FIXED!")
    else:
        print("=" * 60)
        print("❌ FAILED: Issues still remain")
        sys.exit(1)
