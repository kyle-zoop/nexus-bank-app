#!/usr/bin/env python3
"""
Test script to demonstrate gap-filling in transaction history
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from datetime import datetime, timedelta
from bank.user_data import FAKE_ACCOUNTS
from bank.transaction_generator import (
    add_user_transaction, 
    regenerate_all_transactions_preserve_user,
    get_transaction_summary,
    mark_existing_transactions_as_system,
    separate_user_and_system_transactions
)

def create_gap_scenario():
    """Create a scenario with a gap in transaction history"""
    print("=" * 60)
    print("Testing Gap-Filling Transaction System")
    print("=" * 60)
    
    # Test user: janderson47 (middle class)
    username = 'janderson47'
    user_data = FAKE_ACCOUNTS[username]
    
    print(f"\n1. Setting up gap scenario for {username}...")
    
    # First, mark existing transactions as system-generated
    mark_existing_transactions_as_system()
    
    # Clear out existing transactions to create a clean test
    user_data['accounts']['checking']['transactions'] = []
    
    # Add an old system transaction (simulate last activity was 3 weeks ago)
    three_weeks_ago = (datetime.now() - timedelta(days=21)).strftime('%Y-%m-%d')
    old_transaction = {
        'date': three_weeks_ago,
        'description': 'Grocery Store',
        'amount': -85.50,
        'balance': 2398.52,
        'type': 'system_generated',
        'generated_date': datetime.now().isoformat()
    }
    user_data['accounts']['checking']['transactions'].append(old_transaction)
    
    print(f"   ✅ Created old transaction on {three_weeks_ago}")
    
    # Now add some recent user transactions (simulate user becoming active again)
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Manually add user transactions to simulate recent activity
    user_transaction_1 = {
        'date': yesterday,
        'description': 'ATM Withdrawal',
        'amount': -100.00,
        'balance': 2213.02,
        'type': 'user_made',
        'created_date': datetime.now().isoformat()
    }
    
    user_transaction_2 = {
        'date': today,
        'description': 'Direct Deposit - Freelance Work',
        'amount': 500.00,
        'balance': 2713.02,
        'type': 'user_made',
        'created_date': datetime.now().isoformat()
    }
    
    user_data['accounts']['checking']['transactions'].insert(0, user_transaction_2)
    user_data['accounts']['checking']['transactions'].insert(1, user_transaction_1)
    user_data['accounts']['checking']['balance'] = 2713.02
    
    print(f"   ✅ Added user transactions on {yesterday} and {today}")
    
    # Show the current state
    checking_transactions = user_data['accounts']['checking']['transactions']
    user_transactions, system_transactions = separate_user_and_system_transactions(checking_transactions)
    
    print(f"\n2. Current state before gap filling:")
    print(f"   Total transactions: {len(checking_transactions)}")
    print(f"   User-made: {len(user_transactions)}")
    print(f"   System-generated: {len(system_transactions)}")
    print(f"   Date range: {three_weeks_ago} to {today}")
    print(f"   Gap size: ~20 days")
    
    # Show transaction dates
    transaction_dates = sorted([t['date'] for t in checking_transactions])
    print(f"   Transaction dates: {transaction_dates}")
    
    return username

def test_gap_filling():
    """Test the gap-filling functionality"""
    username = create_gap_scenario()
    user_data = FAKE_ACCOUNTS[username]
    
    print(f"\n3. Running gap-filling regeneration...")
    regenerate_all_transactions_preserve_user()
    print("   ✅ Gap-filling completed")
    
    # Check the results
    checking_transactions = user_data['accounts']['checking']['transactions']
    user_transactions, system_transactions = separate_user_and_system_transactions(checking_transactions)
    
    print(f"\n4. Results after gap filling:")
    print(f"   Total transactions: {len(checking_transactions)}")
    print(f"   User-made: {len(user_transactions)}")
    print(f"   System-generated: {len(system_transactions)}")
    
    # Show all transaction dates to verify gap is filled
    all_dates = sorted([t['date'] for t in checking_transactions])
    print(f"\n5. Transaction dates after gap filling:")
    for i, date in enumerate(all_dates):
        transaction = next(t for t in checking_transactions if t['date'] == date)
        transaction_type = transaction.get('type', 'unknown')
        print(f"   {i+1:2d}. {date} - {transaction['description'][:30]:30s} ({transaction_type})")
    
    # Verify user transactions are preserved
    print(f"\n6. Verifying user transactions are preserved:")
    user_transaction_descriptions = [t['description'] for t in user_transactions]
    print(f"   User transactions: {user_transaction_descriptions}")
    
    # Check for gaps
    date_objects = [datetime.strptime(date, '%Y-%m-%d') for date in all_dates]
    gaps = []
    for i in range(len(date_objects) - 1):
        gap_days = (date_objects[i] - date_objects[i+1]).days
        if gap_days > 3:  # More than 3 days gap
            gaps.append(f"{date_objects[i+1].strftime('%Y-%m-%d')} to {date_objects[i].strftime('%Y-%m-%d')} ({gap_days} days)")
    
    print(f"\n7. Gap analysis:")
    if gaps:
        print(f"   ❌ Remaining gaps found:")
        for gap in gaps:
            print(f"      {gap}")
    else:
        print(f"   ✅ No significant gaps found (>3 days)")
    
    print("\n" + "=" * 60)
    if len(system_transactions) > 1 and not gaps:
        print("🎉 SUCCESS: Gap-filling worked! Transaction history is continuous.")
    else:
        print("⚠️  PARTIAL: Some gaps may remain, but user transactions are preserved.")
    print("=" * 60)

if __name__ == "__main__":
    test_gap_filling()
    print("\n🔧 Gap-filling test complete!")
