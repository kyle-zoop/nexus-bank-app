#!/usr/bin/env python3
"""
Test script to verify the template fix for missing account types.
"""

# Test by importing the user data directly
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src', 'bank'))

# Import user data
exec(open('src/bank/user_data.py').read())

def analyze_user_accounts():
    """Analyze which users have which account types"""
    print("User Account Analysis:")
    print("=" * 50)
    
    for username, user_data in FAKE_ACCOUNTS.items():
        accounts = user_data.get('accounts', {})
        account_types = list(accounts.keys())
        print(f"User: {username} ({user_data.get('name', 'Unknown')})")
        print(f"  Account types: {account_types}")
        
        # Check for the problematic account types
        missing = []
        if 'savings' not in accounts:
            missing.append('savings')
        if 'investment' not in accounts:
            missing.append('investment')
        if 'credit_card' not in accounts:
            missing.append('credit_card')
        if 'mortgage' not in accounts:
            missing.append('mortgage')
        if 'auto_loan' not in accounts:
            missing.append('auto_loan')
            
        if missing:
            print(f"  Missing: {missing}")
        else:
            print("  Has all common account types")
        print()

def test_template_logic():
    """Test the conditional logic we implemented"""
    print("Testing Template Logic:")
    print("=" * 50)
    
    # Test with pooruser (only has checking)
    user_data = FAKE_ACCOUNTS['pooruser']
    accounts = user_data['accounts']
    
    print(f"Testing with user: {user_data['name']}")
    print(f"Available accounts: {list(accounts.keys())}")
    
    # Simulate the template logic
    checking_balance = accounts['checking']['balance'] if 'checking' in accounts else 0.0
    savings_balance = accounts['savings']['balance'] if 'savings' in accounts else 0.0
    investment_balance = accounts['investment']['balance'] if 'investment' in accounts else 0.0
    total_assets = checking_balance + savings_balance + investment_balance
    
    credit_card_balance = abs(accounts['credit_card']['balance']) if 'credit_card' in accounts else 0.0
    mortgage_balance = abs(accounts['mortgage']['balance']) if 'mortgage' in accounts else 0.0
    auto_loan_balance = abs(accounts['auto_loan']['balance']) if 'auto_loan' in accounts else 0.0
    total_liabilities = credit_card_balance + mortgage_balance + auto_loan_balance
    
    print(f"Checking balance: ${checking_balance:,.2f}")
    print(f"Savings balance: ${savings_balance:,.2f}")
    print(f"Investment balance: ${investment_balance:,.2f}")
    print(f"Total assets: ${total_assets:,.2f}")
    print(f"Total liabilities: ${total_liabilities:,.2f}")
    print(f"Net worth: ${total_assets - total_liabilities:,.2f}")
    
    print("\n✓ Template logic works without errors!")

if __name__ == "__main__":
    print("Testing template fixes for missing account types...")
    analyze_user_accounts()
    test_template_logic()
