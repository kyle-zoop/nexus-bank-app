#!/usr/bin/env python3
"""
Test script to verify scammer bait transactions persist during regeneration
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.bank.user_data import FAKE_ACCOUNTS
from src.bank.transaction_generator import add_manual_transaction, regenerate_all_transactions_preserve_user

def main():
    print("=" * 70)
    print("🧪 Testing Scammer Bait Transaction Persistence")
    print("=" * 70)
    
    username = 'janderson47'
    account = 'checking'
    
    # Show initial state
    initial_transactions = FAKE_ACCOUNTS[username]['accounts'][account]['transactions']
    initial_count = len(initial_transactions)
    initial_balance = FAKE_ACCOUNTS[username]['accounts'][account]['balance']
    
    print(f"📊 Initial state for {username}/{account}:")
    print(f"   Balance: ${initial_balance:,.2f}")
    print(f"   Transactions: {initial_count}")
    print()
    
    # Add some scammer bait transactions
    print("🎯 Adding scammer bait transactions...")
    
    bait_transactions = [
        ("🎰 FAKE LOTTERY WIN - SCAMMER BAIT", 50000.00, 'scammer_bait'),
        ("⚠️ SUSPICIOUS ACTIVITY DETECTED", -1500.00, 'scammer_bait'),
        ("🚨 FBI INVESTIGATION HOLD", -5000.00, 'scammer_bait'),
        ("💰 NIGERIAN PRINCE INHERITANCE", 75000.00, 'scammer_bait')
    ]
    
    for desc, amount, tx_type in bait_transactions:
        success = add_manual_transaction(username, account, desc, amount, transaction_type=tx_type)
        if success:
            print(f"   ✅ Added: {desc} (${amount:,.2f})")
        else:
            print(f"   ❌ Failed: {desc}")
    
    # Check state after adding bait
    after_bait_transactions = FAKE_ACCOUNTS[username]['accounts'][account]['transactions']
    after_bait_count = len(after_bait_transactions)
    after_bait_balance = FAKE_ACCOUNTS[username]['accounts'][account]['balance']
    
    print()
    print(f"📊 After adding bait transactions:")
    print(f"   Balance: ${after_bait_balance:,.2f}")
    print(f"   Transactions: {after_bait_count}")
    
    # Count bait transactions
    bait_count = sum(1 for t in after_bait_transactions 
                    if t.get('type') == 'scammer_bait' or t.get('admin_added'))
    print(f"   Scammer bait: {bait_count}")
    print()
    
    # Show recent transactions
    print("🔍 Recent transactions (top 10):")
    for i, t in enumerate(after_bait_transactions[:10], 1):
        emoji = "🎯" if t.get('type') == 'scammer_bait' else "💳"
        print(f"  {i:2d}. {emoji} {t['date']} - {t['description'][:50]}")
        print(f"       ${t['amount']:>10,.2f} | Balance: ${t['balance']:,.2f}")
    print()
    
    # NOW THE CRITICAL TEST: Regenerate transactions
    print("🔄 CRITICAL TEST: Regenerating all transactions...")
    print("   (This should preserve all scammer bait transactions)")
    
    success = regenerate_all_transactions_preserve_user()
    
    if success:
        print("   ✅ Regeneration completed successfully!")
    else:
        print("   ❌ Regeneration failed!")
        return
    
    # Check final state
    final_transactions = FAKE_ACCOUNTS[username]['accounts'][account]['transactions']
    final_count = len(final_transactions)
    final_balance = FAKE_ACCOUNTS[username]['accounts'][account]['balance']
    
    # Count preserved bait transactions
    final_bait_count = sum(1 for t in final_transactions 
                          if t.get('type') == 'scammer_bait' or t.get('admin_added'))
    
    print()
    print(f"📊 Final state after regeneration:")
    print(f"   Balance: ${final_balance:,.2f}")
    print(f"   Transactions: {final_count}")
    print(f"   Scammer bait preserved: {final_bait_count}")
    print()
    
    # Verify all bait transactions are still there
    print("🔍 Verifying bait transaction preservation:")
    bait_descriptions = [desc for desc, _, _ in bait_transactions]
    preserved_baits = []
    
    for transaction in final_transactions:
        if transaction.get('type') == 'scammer_bait' or transaction.get('admin_added'):
            preserved_baits.append(transaction['description'])
    
    all_preserved = True
    for expected_desc in bait_descriptions:
        if any(expected_desc in preserved for preserved in preserved_baits):
            print(f"   ✅ PRESERVED: {expected_desc}")
        else:
            print(f"   ❌ LOST: {expected_desc}")
            all_preserved = False
    
    print()
    print("=" * 70)
    if all_preserved and final_bait_count == len(bait_transactions):
        print("🎉 SUCCESS! All scammer bait transactions survived regeneration!")
        print("🎯 Your manual transactions will persist through admin regeneration!")
    else:
        print("❌ FAILURE! Some scammer bait transactions were lost!")
        print(f"   Expected: {len(bait_transactions)} bait transactions")
        print(f"   Found: {final_bait_count} bait transactions")
    print("=" * 70)

if __name__ == "__main__":
    main()
