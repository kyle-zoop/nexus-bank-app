#!/usr/bin/env python3
"""
Direct template test for moment.js fix
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from bank.app import app
from bank.user_data import FAKE_ACCOUNTS

def test_template_direct():
    """Test template rendering directly"""
    print("Testing templates directly...")
    
    with app.app_context():
        try:
            # Test wire verification template
            print("  Testing wire_verification.html...")
            from flask import render_template
            
            # Mock user data
            user_data = FAKE_ACCOUNTS['janderson47']
            
            # Test rendering wire verification template
            html = render_template('wire_verification.html', user=user_data)
            
            if 'moment()' in html:
                print("    ❌ Template still contains moment() references")
                return False
            else:
                print("    ✅ No moment() references found")
                
            # Check if reference number is generated
            if 'WTR-' in html:
                print("    ✅ Reference number is generated correctly")
            else:
                print("    ❌ Reference number not found")
                return False
                
            # Test wire confirmation template
            print("  Testing wire_confirmation.html...")
            html = render_template('wire_confirmation.html', user=user_data)
            
            if 'moment()' in html:
                print("    ❌ Template still contains moment() references")
                return False
            else:
                print("    ✅ No moment() references found")
                
            if 'WTR-' in html:
                print("    ✅ Reference number is generated correctly")
            else:
                print("    ❌ Reference number not found")
                return False
                
            return True
            
        except Exception as e:
            print(f"    ❌ Error: {e}")
            import traceback
            traceback.print_exc()
            return False

if __name__ == "__main__":
    print("=" * 60)
    
    if test_template_direct():
        print("=" * 60)
        print("🎉 SUCCESS: Templates render correctly without moment.js!")
        print("✅ The UndefinedError: 'moment' is undefined issue has been fixed!")
    else:
        print("=" * 60)
        print("❌ FAILED: Templates still have issues")
        sys.exit(1)
