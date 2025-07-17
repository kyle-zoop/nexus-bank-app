#!/usr/bin/env python3
"""
Simple test to verify template fix
"""

import os
import sys

# Change to the project directory 
os.chdir(r'c:\Projects\bank')
sys.path.insert(0, os.path.join(os.getcwd(), 'src'))

print("Current directory:", os.getcwd())
print("Python path:", sys.path[0])

# Test the import
try:
    from bank.user_data import FAKE_ACCOUNTS
    print("✓ Successfully imported FAKE_ACCOUNTS")
    
    # Check pooruser accounts
    pooruser = FAKE_ACCOUNTS.get('pooruser')
    if pooruser:
        print(f"✓ Found pooruser: {pooruser['name']}")
        accounts = pooruser['accounts']
        print(f"✓ pooruser accounts: {list(accounts.keys())}")
        
        # Test the logic that caused the error
        has_savings = 'savings' in accounts
        has_investment = 'investment' in accounts
        has_credit_card = 'credit_card' in accounts
        has_mortgage = 'mortgage' in accounts
        has_auto_loan = 'auto_loan' in accounts
        
        print(f"Has savings: {has_savings}")
        print(f"Has investment: {has_investment}")
        print(f"Has credit_card: {has_credit_card}")
        print(f"Has mortgage: {has_mortgage}")
        print(f"Has auto_loan: {has_auto_loan}")
        
        # Test the fixed template logic
        checking_balance = accounts['checking']['balance'] if 'checking' in accounts else 0.0
        savings_balance = accounts['savings']['balance'] if 'savings' in accounts else 0.0
        investment_balance = accounts['investment']['balance'] if 'investment' in accounts else 0.0
        
        print(f"\nTemplate logic test:")
        print(f"Checking balance: ${checking_balance:,.2f}")
        print(f"Savings balance: ${savings_balance:,.2f}")
        print(f"Investment balance: ${investment_balance:,.2f}")
        print(f"Total assets: ${checking_balance + savings_balance + investment_balance:,.2f}")
        
        print("\n✓ Template logic works without errors!")
    else:
        print("✗ pooruser not found")
        
except ImportError as e:
    print(f"✗ Import failed: {e}")
except Exception as e:
    print(f"✗ Error: {e}")
