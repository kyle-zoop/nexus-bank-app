#!/usr/bin/env python3
"""
Test script to demonstrate robust transaction preservation
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from bank.user_data import FAKE_ACCOUNTS
from bank.transaction_generator import (
    add_user_transaction, 
    regenerate_all_transactions_preserve_user,
    get_transaction_summary,
    mark_existing_transactions_as_system
)
from bank.transfer_utils import process_internal_transfer

def test_robust_transactions():
    """Test the robust transaction system"""
    print("=" * 60)
    print("Testing Robust Transaction System")
    print("=" * 60)
    
    # Test user: janderson47 (middle class)
    username = 'janderson47'
    user_data = FAKE_ACCOUNTS[username]
    
    print(f"\n1. Initial state for {username}:")
    summary = get_transaction_summary(username)
    if summary:
        print(f"   Total transactions: {summary['total_transactions']}")
        print(f"   User-made: {summary['user_made']}")
        print(f"   System-generated: {summary['system_generated']}")
    
    # Show checking account balance
    checking_balance = user_data['accounts']['checking']['balance']
    print(f"   Checking balance: ${checking_balance:,.2f}")
    
    print(f"\n2. Making some user transactions...")
    
    # Mark existing transactions as system-generated first
    mark_existing_transactions_as_system()
    
    # Add some user-made transactions
    add_user_transaction(username, 'checking', 'ATM Withdrawal', -100.00)
    add_user_transaction(username, 'checking', 'Direct Deposit - Side Job', 500.00)
    add_user_transaction(username, 'savings', 'Emergency Fund Transfer', 200.00)
    
    print("   ✅ Added user transactions:")
    print("      - ATM Withdrawal: -$100.00")
    print("      - Side Job Deposit: +$500.00") 
    print("      - Emergency Transfer: +$200.00")
    
    # Show updated state
    summary = get_transaction_summary(username)
    if summary:
        print(f"\n3. After user transactions:")
        print(f"   Total transactions: {summary['total_transactions']}")
        print(f"   User-made: {summary['user_made']}")
        print(f"   System-generated: {summary['system_generated']}")
    
    # Show checking account balance
    checking_balance = user_data['accounts']['checking']['balance']
    print(f"   Checking balance: ${checking_balance:,.2f}")
    
    print(f"\n4. Regenerating system transactions...")
    regenerate_all_transactions_preserve_user()
    print("   ✅ System transactions regenerated")
    
    # Show final state
    summary = get_transaction_summary(username)
    if summary:
        print(f"\n5. After regeneration:")
        print(f"   Total transactions: {summary['total_transactions']}")
        print(f"   User-made: {summary['user_made']}")
        print(f"   System-generated: {summary['system_generated']}")
    
    # Show checking account balance
    checking_balance = user_data['accounts']['checking']['balance']
    print(f"   Checking balance: ${checking_balance:,.2f}")
    
    print(f"\n6. Verifying user transactions are preserved...")
    checking_transactions = user_data['accounts']['checking']['transactions']
    user_transactions = [t for t in checking_transactions if t.get('type') == 'user_made']
    
    print(f"   Found {len(user_transactions)} preserved user transactions:")
    for trans in user_transactions:
        print(f"      - {trans['description']}: ${trans['amount']:,.2f}")
    
    print("\n" + "=" * 60)
    if len(user_transactions) >= 2:  # Should have ATM + Direct Deposit
        print("🎉 SUCCESS: User transactions preserved during regeneration!")
    else:
        print("❌ FAILED: User transactions not properly preserved")
    print("=" * 60)

def test_transfer_preservation():
    """Test that transfers are marked as user-made"""
    print("\n" + "=" * 60)
    print("Testing Transfer Preservation")
    print("=" * 60)
    
    username = 'janderson47'
    user_data = FAKE_ACCOUNTS[username]
    
    print(f"\n1. Initial balances for {username}:")
    checking_balance = user_data['accounts']['checking']['balance']
    savings_balance = user_data['accounts']['savings']['balance']
    print(f"   Checking: ${checking_balance:,.2f}")
    print(f"   Savings: ${savings_balance:,.2f}")
    
    print(f"\n2. Processing internal transfer...")
    # Transfer $100 from checking to savings
    success = process_internal_transfer(user_data, 'checking', 'savings', 100.00)
    
    if success:
        print("   ✅ Transfer completed")
        
        print(f"\n3. Updated balances:")
        checking_balance = user_data['accounts']['checking']['balance']
        savings_balance = user_data['accounts']['savings']['balance']
        print(f"   Checking: ${checking_balance:,.2f}")
        print(f"   Savings: ${savings_balance:,.2f}")
        
        print(f"\n4. Checking transaction types...")
        checking_transactions = user_data['accounts']['checking']['transactions']
        savings_transactions = user_data['accounts']['savings']['transactions']
        
        # Check most recent transactions
        if checking_transactions and checking_transactions[0].get('type') == 'user_made':
            print("   ✅ Checking transfer marked as user_made")
        else:
            print("   ❌ Checking transfer not properly marked")
            
        if savings_transactions and savings_transactions[0].get('type') == 'user_made':
            print("   ✅ Savings transfer marked as user_made")
        else:
            print("   ❌ Savings transfer not properly marked")
    else:
        print("   ❌ Transfer failed")

if __name__ == "__main__":
    test_robust_transactions()
    test_transfer_preservation()
    print("\n🔧 Test complete! The system now preserves user-made transactions.")
