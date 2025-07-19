#!/usr/bin/env python3
"""
Test script to verify that the moment.js fix works properly
"""

import requests
import sys

def test_wire_verification():
    """Test the wire verification page to ensure moment.js errors are fixed"""
    try:
        # Test with sample parameters
        url = "http://127.0.0.1:5000/wire-verification"
        params = {
            'amount': '5000.00',
            'recipient_name': 'Test Recipient',
            'bank_name': 'Test Bank',
            'bank_country': 'Australia',
            'purpose': 'Test Transfer'
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            print("✅ Wire verification page loads successfully")
            
            # Check if the page contains the expected reference number format
            if "WTR-" in response.text and len([line for line in response.text.split('\n') if 'WTR-' in line]) > 0:
                print("✅ Reference number generation works correctly")
            else:
                print("❌ Reference number generation may have issues")
                
            # Check for any remaining moment() references
            if "moment()" in response.text:
                print("❌ Still contains moment() references")
                return False
            else:
                print("✅ No moment() references found")
                
            return True
        else:
            print(f"❌ Page returned status code: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to the Flask application. Make sure it's running on http://127.0.0.1:5000")
        return False
    except Exception as e:
        print(f"❌ Error testing wire verification: {e}")
        return False

def test_wire_confirmation():
    """Test the wire confirmation page"""
    try:
        url = "http://127.0.0.1:5000/wire-confirmation"
        params = {
            'amount': '5000.00',
            'recipient_name': 'Test Recipient',
            'bank_name': 'Test Bank'
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            print("✅ Wire confirmation page loads successfully")
            
            # Check for any remaining moment() references
            if "moment()" in response.text:
                print("❌ Still contains moment() references")
                return False
            else:
                print("✅ No moment() references found")
                
            return True
        else:
            print(f"❌ Page returned status code: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing wire confirmation: {e}")
        return False

if __name__ == "__main__":
    print("Testing moment.js fix...")
    print("=" * 50)
    
    success = True
    success &= test_wire_verification()
    success &= test_wire_confirmation()
    
    print("=" * 50)
    if success:
        print("🎉 All tests passed! The moment.js issue has been fixed.")
        sys.exit(0)
    else:
        print("❌ Some tests failed. Please check the output above.")
        sys.exit(1)
