#!/usr/bin/env python3
"""
Quick test to verify the gap-filling works through the web interface
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.bank.user_data import FAKE_ACCOUNTS
from src.bank.transaction_generator import regenerate_all_transactions_preserve_user
from datetime import datetime, timedelta
import random

def main():
    print("=" * 60)
    print("Quick Web Interface Gap-Filling Test")
    print("=" * 60)
    
    # Pick a user and create a gap scenario
    username = 'janderson47'
    account_name = 'checking'
    
    print(f"1. Setting up gap scenario for {username}...")
    
    # Clear existing transactions
    FAKE_ACCOUNTS[username]['accounts'][account_name]['transactions'] = []
    
    # Add an old transaction
    old_date = (datetime.now() - timedelta(days=25)).strftime('%Y-%m-%d')
    old_transaction = {
        'date': old_date,
        'description': 'Old System Transaction',
        'amount': -45.0,
        'balance': 3500.0,
        'type': 'system_generated'
    }
    FAKE_ACCOUNTS[username]['accounts'][account_name]['transactions'].append(old_transaction)
    
    # Add recent user transaction
    recent_date = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')
    user_transaction = {
        'date': recent_date,
        'description': 'User Transfer',
        'amount': -200.0,
        'balance': 3300.0,
        'type': 'user_made'
    }
    FAKE_ACCOUNTS[username]['accounts'][account_name]['transactions'].append(user_transaction)
    
    print(f"   ✅ Created old transaction on {old_date}")
    print(f"   ✅ Created user transaction on {recent_date}")
    print(f"   📅 Gap size: ~23 days")
    
    # Check before regeneration
    transactions_before = FAKE_ACCOUNTS[username]['accounts'][account_name]['transactions']
    print(f"2. Before regeneration: {len(transactions_before)} transactions")
    
    # Run the regeneration (same as admin panel would do)
    print("3. Running regeneration (simulating admin panel)...")
    success = regenerate_all_transactions_preserve_user()
    
    if success:
        print("   ✅ Regeneration completed successfully")
    else:
        print("   ❌ Regeneration failed")
        return
    
    # Check results
    transactions_after = FAKE_ACCOUNTS[username]['accounts'][account_name]['transactions']
    user_transactions = [t for t in transactions_after if t.get('type') == 'user_made']
    system_transactions = [t for t in transactions_after if t.get('type') == 'system_generated']
    
    print(f"4. After regeneration:")
    print(f"   Total transactions: {len(transactions_after)}")
    print(f"   User-made: {len(user_transactions)}")
    print(f"   System-generated: {len(system_transactions)}")
    
    # Check for gaps
    transaction_dates = sorted([t['date'] for t in transactions_after])
    gaps = []
    for i in range(1, len(transaction_dates)):
        date1 = datetime.strptime(transaction_dates[i-1], '%Y-%m-%d')
        date2 = datetime.strptime(transaction_dates[i], '%Y-%m-%d')
        gap_days = (date2 - date1).days
        if gap_days > 3:
            gaps.append((transaction_dates[i-1], transaction_dates[i], gap_days))
    
    print(f"5. Gap analysis:")
    if gaps:
        print(f"   ⚠️ Found {len(gaps)} significant gaps (>3 days):")
        for gap in gaps:
            print(f"      {gap[0]} to {gap[1]}: {gap[2]} days")
    else:
        print("   ✅ No significant gaps found!")
    
    # Verify user transaction preserved
    user_preserved = any(t.get('description') == 'User Transfer' for t in transactions_after)
    print(f"6. User transaction preservation: {'✅ Preserved' if user_preserved else '❌ Lost'}")
    
    print("=" * 60)
    if not gaps and user_preserved:
        print("🎉 SUCCESS: Web interface gap-filling working perfectly!")
    else:
        print("⚠️ ISSUE: Some problems detected")
    print("=" * 60)

if __name__ == "__main__":
    main()
