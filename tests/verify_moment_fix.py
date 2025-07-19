#!/usr/bin/env python3
"""
Test to verify moment.js fix
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from bank.app import app

def test_moment_fix():
    """Test that templates render without moment.js errors"""
    print("Testing moment.js fix...")
    
    with app.test_client() as client:
        try:
            # Test wire verification page
            print("  Testing wire verification page...")
            response = client.get('/wire_verification?amount=5000.00&recipient_name=Test&bank_name=TestBank&bank_country=Australia&purpose=Test')
            
            if response.status_code == 200:
                print("    ✅ Wire verification page renders successfully")
                if b'moment()' not in response.data:
                    print("    ✅ No moment() references found")
                else:
                    print("    ❌ Still contains moment() references")
                    return False
            else:
                print(f"    ❌ Failed with status: {response.status_code}")
                return False
                
            # Test wire confirmation page  
            print("  Testing wire confirmation page...")
            response = client.get('/wire_confirmation?amount=5000.00&recipient_name=Test&bank_name=TestBank')
            
            if response.status_code == 200:
                print("    ✅ Wire confirmation page renders successfully")
                if b'moment()' not in response.data:
                    print("    ✅ No moment() references found")
                else:
                    print("    ❌ Still contains moment() references")
                    return False
            else:
                print(f"    ❌ Failed with status: {response.status_code}")
                return False
                
            return True
            
        except Exception as e:
            print(f"    ❌ Error: {e}")
            return False

if __name__ == "__main__":
    print("=" * 50)
    
    if test_moment_fix():
        print("=" * 50)
        print("🎉 SUCCESS: moment.js fix is working!")
    else:
        print("=" * 50)
        print("❌ FAILED: moment.js issues remain")
        sys.exit(1)
