#!/usr/bin/env python3
"""
Test script for manual transaction functionality
Demonstrates how to counter scammer source code edits
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.bank.user_data import FAKE_ACCOUNTS
from src.bank.transaction_generator import add_manual_transaction

def main():
    print("=" * 70)
    print("🎯 SCAM BAIT: Manual Transaction Testing")
    print("=" * 70)
    
    # Scenario: Scammer edits source to show fake $50,000 lottery win
    username = 'janderson47'
    account = 'checking'
    
    print(f"📊 Current balance for {username} checking: ${FAKE_ACCOUNTS[username]['accounts'][account]['balance']:,.2f}")
    print()
    
    print("🚨 SCENARIO: Scammer edits HTML to show fake $50,000 lottery deposit")
    print("💡 COUNTER-MOVE: Add the transaction to make it 'real' and mess with them")
    print()
    
    # Add the "lottery" transaction 
    success = add_manual_transaction(
        username=username,
        account_name=account,
        description="🎰 MEGA LOTTERY JACKPOT - CONGRATULATIONS! 🎰",
        amount=50000.00,
        transaction_type='scammer_bait'
    )
    
    if success:
        print("✅ Added fake lottery transaction!")
        print(f"💰 New balance: ${FAKE_ACCOUNTS[username]['accounts'][account]['balance']:,.2f}")
        print()
        
        # Show recent transactions
        transactions = FAKE_ACCOUNTS[username]['accounts'][account]['transactions'][:5]
        print("📋 Recent transactions:")
        for i, t in enumerate(transactions, 1):
            emoji = "🎯" if t.get('type') == 'scammer_bait' else "💳"
            print(f"  {i}. {emoji} {t['date']} - {t['description']}")
            print(f"      Amount: ${t['amount']:,.2f} | Balance: ${t['balance']:,.2f}")
        print()
        
        print("🎭 PSYCHOLOGICAL WARFARE IDEAS:")
        print("  • Add suspicious 'IRS Investigation' charges")
        print("  • Add 'Account Frozen - Contact Legal Dept' fees") 
        print("  • Add competing scammer 'deposits' to create confusion")
        print("  • Add 'Money Laundering Detection' alerts")
        print()
        
        # Demonstrate adding a suspicious transaction
        print("🔥 Adding suspicious transaction to really mess with them...")
        add_manual_transaction(
            username=username,
            account_name=account,
            description="⚠️ SUSPICIOUS ACTIVITY DETECTED - ACCOUNT FLAGGED",
            amount=-1500.00,
            transaction_type='scammer_bait'
        )
        
        print("✅ Added account flag fee!")
        print(f"💸 New balance: ${FAKE_ACCOUNTS[username]['accounts'][account]['balance']:,.2f}")
        print()
        
        print("🎬 RESULT: Scammer thinks they successfully added fake money,")
        print("          but now they see suspicious charges they didn't add!")
        print("          They'll be confused and paranoid about being detected.")
        
    else:
        print("❌ Failed to add transaction")
    
    print("=" * 70)
    print("🎯 Manual transaction testing complete!")
    print("💡 Use the admin panel to add these in real-time during scam calls!")
    print("=" * 70)

if __name__ == "__main__":
    main()
