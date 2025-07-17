#!/usr/bin/env python3
"""
Quick test of expanded transaction data
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from bank.user_data import FAKE_ACCOUNTS
    
    print("🎉 EXPANDED TRANSACTION DATA TEST")
    print("=" * 50)
    
    for username, user_data in FAKE_ACCOUNTS.items():
        name = user_data['name']
        account_count = len(user_data['accounts'])
        
        print(f"\n👤 {name} ({username})")
        print(f"   📊 Accounts: {account_count}")
        
        total_transactions = 0
        for account_type, account in user_data['accounts'].items():
            transaction_count = len(account.get('transactions', []))
            total_transactions += transaction_count
            print(f"   📋 {account_type}: {transaction_count} transactions")
        
        print(f"   🔢 Total transactions: {total_transactions}")
    
    print(f"\n✅ All {len(FAKE_ACCOUNTS)} user profiles loaded successfully!")
    print("✅ Extensive transaction history added for realistic banking experience!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
