#!/usr/bin/env python3
"""
Comprehensive test to verify the Jinja2 template fix
"""

import sys
import os
import tempfile

# Setup paths
project_dir = r'c:\Projects\bank'
sys.path.insert(0, os.path.join(project_dir, 'src'))

# Create a minimal Flask app to test template rendering
from flask import Flask, render_template

def create_test_app():
    """Create a minimal Flask app for testing"""
    return Flask(__name__, 
                 template_folder=os.path.join(project_dir, 'src', 'bank', 'templates'),
                 static_folder=os.path.join(project_dir, 'src', 'bank', 'static'))

def load_user_data():
    """Load user data from the module"""
    try:
        exec(open(os.path.join(project_dir, 'src', 'bank', 'user_data.py')).read(), globals())
        return globals()['FAKE_ACCOUNTS']
    except Exception as e:
        print(f"Error loading user data: {e}")
        return None

def test_template_rendering():
    """Test template rendering for all users"""
    print("Testing Template Rendering")
    print("=" * 50)
    
    fake_accounts = load_user_data()
    if not fake_accounts:
        print("Failed to load user data")
        return False
    
    app = create_test_app()
    
    templates_to_test = ['dashboard.html', 'statements.html']
    all_passed = True
    
    with app.app_context():
        for username, user_data in fake_accounts.items():
            print(f"\nTesting user: {username} ({user_data.get('name', 'Unknown')})")
            print(f"Accounts: {list(user_data.get('accounts', {}).keys())}")
            
            for template_name in templates_to_test:
                try:
                    rendered = render_template(template_name, user=user_data, username=username)
                    print(f"  ✓ {template_name}: Success ({len(rendered)} chars)")
                except Exception as e:
                    print(f"  ✗ {template_name}: ERROR - {e}")
                    all_passed = False
    
    return all_passed

def test_account_analysis():
    """Analyze account types across users"""
    print("\nAccount Type Analysis")
    print("=" * 50)
    
    fake_accounts = load_user_data()
    if not fake_accounts:
        return False
    
    all_account_types = set()
    
    for username, user_data in fake_accounts.items():
        accounts = user_data.get('accounts', {})
        account_types = set(accounts.keys())
        all_account_types.update(account_types)
        
        print(f"{username}: {sorted(account_types)}")
    
    print(f"\nAll account types found: {sorted(all_account_types)}")
    
    # Check which users are missing which account types
    print("\nMissing account types:")
    common_types = ['checking', 'savings', 'investment', 'credit_card', 'mortgage', 'auto_loan']
    
    for username, user_data in fake_accounts.items():
        accounts = user_data.get('accounts', {})
        missing = [t for t in common_types if t not in accounts]
        if missing:
            print(f"  {username}: missing {missing}")
    
    return True

def test_template_logic():
    """Test the specific logic that was causing the error"""
    print("\nTesting Template Logic")
    print("=" * 50)
    
    fake_accounts = load_user_data()
    if not fake_accounts:
        return False
    
    # Test with pooruser (the problematic case)
    pooruser = fake_accounts.get('pooruser')
    if not pooruser:
        print("pooruser not found!")
        return False
    
    accounts = pooruser['accounts']
    print(f"Testing with {pooruser['name']}")
    print(f"Available accounts: {list(accounts.keys())}")
    
    # Test the original broken logic (what would fail)
    print("\nOriginal logic (would fail):")
    try:
        # This is what was causing the error
        # total_assets = accounts['checking']['balance'] + accounts['savings']['balance'] + accounts['investment']['balance']
        print("  Would try to access accounts['savings']['balance'] -> UndefinedError")
    except KeyError as e:
        print(f"  ✗ KeyError: {e}")
    
    # Test the fixed logic
    print("\nFixed logic (should work):")
    try:
        checking_balance = accounts['checking']['balance'] if 'checking' in accounts else 0.0
        savings_balance = accounts['savings']['balance'] if 'savings' in accounts else 0.0
        investment_balance = accounts['investment']['balance'] if 'investment' in accounts else 0.0
        total_assets = checking_balance + savings_balance + investment_balance
        
        print(f"  ✓ Checking: ${checking_balance:,.2f}")
        print(f"  ✓ Savings: ${savings_balance:,.2f} (missing account)")
        print(f"  ✓ Investment: ${investment_balance:,.2f} (missing account)")
        print(f"  ✓ Total Assets: ${total_assets:,.2f}")
        
        # Test liabilities too
        credit_card_balance = abs(accounts['credit_card']['balance']) if 'credit_card' in accounts else 0.0
        mortgage_balance = abs(accounts['mortgage']['balance']) if 'mortgage' in accounts else 0.0
        auto_loan_balance = abs(accounts['auto_loan']['balance']) if 'auto_loan' in accounts else 0.0
        total_liabilities = credit_card_balance + mortgage_balance + auto_loan_balance
        
        print(f"  ✓ Total Liabilities: ${total_liabilities:,.2f}")
        print(f"  ✓ Net Worth: ${total_assets - total_liabilities:,.2f}")
        
        return True
    except Exception as e:
        print(f"  ✗ Error in fixed logic: {e}")
        return False

if __name__ == "__main__":
    print("Comprehensive Template Fix Verification")
    print("=" * 60)
    
    # Run all tests
    analysis_ok = test_account_analysis()
    logic_ok = test_template_logic()
    rendering_ok = test_template_rendering()
    
    print("\n" + "=" * 60)
    print("SUMMARY:")
    print(f"Account Analysis: {'✓ PASS' if analysis_ok else '✗ FAIL'}")
    print(f"Template Logic: {'✓ PASS' if logic_ok else '✗ FAIL'}")
    print(f"Template Rendering: {'✓ PASS' if rendering_ok else '✗ FAIL'}")
    
    if analysis_ok and logic_ok and rendering_ok:
        print("\n🎉 ALL TESTS PASSED! The Jinja2 UndefinedError has been fixed.")
        print("The templates now gracefully handle users with missing account types.")
    else:
        print("\n❌ Some tests failed. There may still be issues to resolve.")
        sys.exit(1)
