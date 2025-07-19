#!/usr/bin/env python3
"""
Quick script to regenerate transactions and keep data current
Can be run as a scheduled task or manually
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.bank.transaction_generator import regenerate_all_transactions

if __name__ == '__main__':
    print("🔄 Regenerating transactions for Nexus Bank...")
    
    try:
        regenerate_all_transactions()
        print("✅ Successfully regenerated transactions for all users!")
        print("📅 Data is now current up to today's date.")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
