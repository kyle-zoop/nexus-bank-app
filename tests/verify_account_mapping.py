#!/usr/bin/env python3
"""
Test script to verify user account mapping in admin panel
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.bank.user_data import FAKE_ACCOUNTS

def main():
    print("=" * 70)
    print("🔍 User Account Mapping Verification")
    print("=" * 70)
    
    print("This shows what accounts each user actually has vs what was")
    print("previously shown in the admin dropdown (all accounts).")
    print()
    
    for username, user_data in FAKE_ACCOUNTS.items():
        name = user_data.get('name', 'Unknown')
        accounts = user_data.get('accounts', {})
        
        print(f"👤 {username} ({name}):")
        
        if accounts:
            for account_name, account_data in accounts.items():
                account_type = account_data.get('account_type', 'Unknown Type')
                balance = account_data.get('balance', 0)
                print(f"   💳 {account_name}: {account_type} (${balance:,.2f})")
        else:
            print("   ❌ No accounts found")
        print()
    
    print("=" * 70)
    print("🔧 JavaScript Mapping in Admin Panel:")
    print("=" * 70)
    
    # Show the mapping that's now in the JavaScript
    mappings = {
        'vhamilton': ['checking', 'savings', 'credit_card', 'mortgage', 'investment'],
        'janderson47': ['checking', 'savings', 'auto_loan'],
        'sbrooks85': ['checking'],
        'emartinez48': ['checking', 'savings'],
        'achen22': ['checking', 'student_loan']
    }
    
    for username, expected_accounts in mappings.items():
        user_data = FAKE_ACCOUNTS[username]
        actual_accounts = list(user_data.get('accounts', {}).keys())
        name = user_data.get('name', 'Unknown')
        
        print(f"👤 {username} ({name}):")
        print(f"   Expected in JS: {expected_accounts}")
        print(f"   Actual in data: {actual_accounts}")
        
        # Check for mismatches
        missing = [acc for acc in actual_accounts if acc not in expected_accounts]
        extra = [acc for acc in expected_accounts if acc not in actual_accounts]
        
        if missing:
            print(f"   ⚠️  Missing from JS: {missing}")
        if extra:
            print(f"   ⚠️  Extra in JS: {extra}")
        if not missing and not extra:
            print(f"   ✅ Perfect match!")
        print()
    
    print("=" * 70)
    print("💡 Benefits of Dynamic Account Dropdown:")
    print("=" * 70)
    print("✅ Users only see accounts they actually have")
    print("✅ Prevents admin errors (trying to add to non-existent accounts)")
    print("✅ More intuitive interface - guided workflow")
    print("✅ Shows proper account names (e.g., 'Executive Platinum Checking')")
    print("✅ Account dropdown disabled until user selected")
    print("=" * 70)

if __name__ == "__main__":
    main()
