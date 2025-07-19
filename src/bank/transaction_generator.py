"""
Transaction generator utility for keeping bank data current
Generates realistic transactions up to the current date
Now with support for preserving user-made transactions
"""
import random
from datetime import datetime, timedelta

# Transaction templates for different user types
WEALTHY_TRANSACTIONS = {
    'checking': {
        'income': [
            'Executive Salary Deposit',
            'Investment Portfolio Transfer',
            'Dividend Payment',
            'Bonus Distribution',
            'Capital Gains Transfer',
            'Private Equity Payout',
            'Trust Fund Distribution'
        ],
        'expenses': [
            'Luxury Car Collection Addition',
            'Private Banking Fee',
            'Art Gallery Commission',
            'Charity Gala Donation',
            'Wine Cellar Investment',
            'Private Island Resort',
            'Private Jet Charter',
            'Yacht Club Membership',
            'Fine Dining Experience',
            'Designer Shopping Spree',
            'Premium Golf Club Fees',
            'Luxury Hotel Suite',
            'Private Art Auction',
            'High-End Jewelry Purchase',
            'Exclusive Wine Tasting',
            'Private Concert Tickets',
            'Helicopter Charter Service',
            'Luxury Spa Treatment'
        ]
    },
    'savings': {
        'income': [
            'High Yield Bond Maturation',
            'Cryptocurrency Portfolio Gains',
            'Real Estate Investment Trust',
            'Private Equity Distribution',
            'Swiss Bank Transfer In',
            'Monthly Interest Compound',
            'Government Bond Interest',
            'Corporate Bond Dividend',
            'Foreign Exchange Gains',
            'Precious Metals Appreciation'
        ],
        'expenses': [
            'Treasury Security Purchase',
            'Investment Rebalancing',
            'Tax Optimization Transfer',
            'Estate Planning Transfer'
        ]
    },
    'credit_card': {
        'expenses': [
            'Private Shopping - Harrods London',
            'Michelin Star Restaurant',
            'Luxury Spa Weekend Package',
            'Designer Jewelry Purchase',
            'Private Yacht Charter',
            'Concierge Services',
            'Premium Wine Collection',
            'First Class Flight Upgrade',
            'Luxury Resort Package',
            'Private Shopping Session',
            'High-End Electronics',
            'Exclusive Event Tickets',
            'Premium Car Rental',
            'Luxury Watch Collection',
            'Designer Fashion Show',
            'Private Chef Services'
        ]
    },
    'investment': {
        'income': [
            'AI Technology Fund Surge',
            'Quantum Computing Stocks',
            'Biotech Portfolio Gains',
            'Green Energy ETF Performance',
            'International Markets Rally',
            'Space Technology IPO',
            'Cryptocurrency Mining Profits',
            'Tech Stock Surge',
            'Healthcare Sector Boom',
            'Renewable Energy Gains',
            'Emerging Markets Growth',
            'Real Estate Appreciation'
        ]
    }
}

MIDDLE_CLASS_TRANSACTIONS = {
    'checking': {
        'income': [
            'Payroll Deposit',
            'Tax Refund',
            'Overtime Pay',
            'Freelance Payment',
            'Side Hustle Income',
            'Government Benefit'
        ],
        'expenses': [
            'Grocery Store',
            'Coffee Shop',
            'ATM Withdrawal',
            'Online Shopping',
            'Movie Tickets',
            'Mobile Phone Bill',
            'Takeaway Dinner',
            'Gas Station',
            'Restaurant',
            'Internet Bill',
            'Rent Payment',
            'Utility Bill',
            'Insurance Payment',
            'Medical Co-pay',
            'Gym Membership',
            'Streaming Service',
            'Public Transport',
            'Parking Fee',
            'Home Maintenance',
            'Car Service'
        ]
    },
    'savings': {
        'income': [
            'Monthly Savings Transfer',
            'Interest Payment',
            'Bonus Deposit',
            'Emergency Fund Addition'
        ],
        'expenses': [
            'Emergency Fund Withdrawal',
            'Home Repair Fund'
        ]
    }
}

POOR_TRANSACTIONS = {
    'checking': {
        'income': [
            'Part-time Job Deposit',
            'Government Assistance',
            'Gig Work Payment',
            'Cash Job Deposit',
            'Refund Credit'
        ],
        'expenses': [
            'Dollar Store',
            'Bus Fare',
            'Fast Food',
            'Laundromat',
            'ATM Fee',
            'ATM Withdrawal',
            'Convenience Store',
            'Coffee Shop',
            'Grocery Store',
            'Phone Card',
            'Thrift Store',
            'Gas Station Snack',
            'Library Fine',
            'Overdraft Fee'
        ]
    }
}

RETIREE_TRANSACTIONS = {
    'checking': {
        'income': [
            'Pension Deposit',
            'Social Security Deposit',
            'Investment Dividend',
            'Retirement Fund Distribution'
        ],
        'expenses': [
            'Senior Center Lunch',
            'Library Book Fine',
            'Pharmacy - Prescription',
            'Garden Center',
            'Grandchildren Visit Treats',
            'Grocery Store - Senior Hours',
            'Church Collection Donation',
            'Medicare Copay',
            'Senior Discount Store',
            'Doctor Visit Copay',
            'Book Club Coffee',
            'Medicare Supplement Premium',
            'Property Tax',
            'Home Insurance',
            'Utility Bill - Electric',
            'HOA Fee'
        ]
    },
    'savings': {
        'income': [
            'Monthly Transfer from Checking',
            'Interest Payment',
            'CD Maturation',
            'Pension Rollover'
        ],
        'expenses': [
            'Emergency Withdrawal',
            'Medical Emergency Fund',
            'Home Repair Fund'
        ]
    }
}

STUDENT_TRANSACTIONS = {
    'checking': {
        'income': [
            'Part-time Job Deposit',
            'Parents Transfer',
            'Student Grant',
            'Textbook Return Refund',
            'Work Study Payment'
        ],
        'expenses': [
            'Campus Meal Card Reload',
            'Study Group Coffee',
            'Online Course Materials',
            'Uber Eats Delivery',
            'ATM Fee',
            'ATM Withdrawal',
            'Energy Drink - Exam Prep',
            'Bookstore',
            'Campus Coffee Shop',
            'Pizza Delivery',
            'Laundry',
            'Dorm Room Snacks',
            'Student Activity Fee',
            'Campus Meal Plan',
            'Study Group Pizza',
            'School Supplies',
            'Campus Parking Fee',
            'Movie Night',
            'Overdraft Fee'
        ]
    }
}

def get_user_transaction_templates(username):
    """Get transaction templates based on user type"""
    if username == 'vhamilton':
        return WEALTHY_TRANSACTIONS
    elif username == 'janderson47':
        return MIDDLE_CLASS_TRANSACTIONS
    elif username == 'sbrooks85':
        return POOR_TRANSACTIONS
    elif username == 'emartinez48':
        return RETIREE_TRANSACTIONS
    elif username == 'achen22':
        return STUDENT_TRANSACTIONS
    else:
        return MIDDLE_CLASS_TRANSACTIONS

def generate_amount(username, account_type, transaction_type):
    """Generate realistic amounts based on user type and account"""
    if username == 'vhamilton':  # Wealthy
        if account_type == 'checking':
            if transaction_type == 'income':
                return random.uniform(50000, 2000000)
            else:
                return -random.uniform(1000, 500000)
        elif account_type == 'savings':
            if transaction_type == 'income':
                return random.uniform(100000, 3000000)
            else:
                return -random.uniform(500000, 2000000)
        elif account_type == 'credit_card':
            return -random.uniform(5000, 150000)
        elif account_type == 'investment':
            return random.uniform(500000, 5000000)
    
    elif username == 'janderson47':  # Middle class
        if account_type == 'checking':
            if transaction_type == 'income':
                return random.uniform(2000, 5000)
            else:
                return -random.uniform(5, 2000)
        elif account_type == 'savings':
            if transaction_type == 'income':
                return random.uniform(100, 500)
            else:
                return -random.uniform(200, 1000)
    
    elif username == 'sbrooks85':  # Poor
        if transaction_type == 'income':
            return random.uniform(20, 100)
        else:
            return -random.uniform(2, 50)
    
    elif username == 'emartinez48':  # Retiree
        if account_type == 'checking':
            if transaction_type == 'income':
                return random.uniform(1500, 2500)
            else:
                return -random.uniform(10, 200)
        elif account_type == 'savings':
            if transaction_type == 'income':
                return random.uniform(400, 600)
            else:
                return -random.uniform(1000, 3000)
    
    elif username == 'achen22':  # Student
        if transaction_type == 'income':
            return random.uniform(150, 400)
        else:
            return -random.uniform(3, 80)
    
    return 0

def generate_new_transactions(user_accounts, username, days_to_generate=7):
    """Generate new transactions for the past N days"""
    templates = get_user_transaction_templates(username)
    today = datetime.now()
    
    for account_name, account_data in user_accounts.items():
        if 'transactions' not in account_data:
            continue
            
        if account_name not in templates:
            continue
            
        # Get existing transaction dates
        existing_dates = set()
        for trans in account_data['transactions']:
            existing_dates.add(trans['date'])
        
        # Generate transactions for missing days
        for i in range(days_to_generate):
            date = (today - timedelta(days=i)).strftime('%Y-%m-%d')
            
            if date in existing_dates:
                continue
            
            # Determine if we should add a transaction (not every day)
            if random.random() > 0.7:  # 30% chance of transaction per day
                continue
            
            # Choose transaction type and description
            account_templates = templates[account_name]
            
            if random.random() < 0.3 and 'income' in account_templates:  # 30% chance of income
                transaction_type = 'income'
                description = random.choice(account_templates['income'])
            else:
                transaction_type = 'expenses'
                description = random.choice(account_templates.get('expenses', account_templates.get('income', ['Transaction'])))
            
            amount = generate_amount(username, account_name, transaction_type)
            
            # Calculate new balance (simplified - in real implementation would need to sort by date)
            current_balance = account_data.get('balance', 0)
            new_balance = current_balance + amount
            
            new_transaction = {
                'date': date,
                'description': description,
                'amount': amount,
                'balance': new_balance,
                'type': 'system_generated',  # Mark as system-generated
                'generated_date': datetime.now().isoformat()
            }
            
            # Insert at the beginning (most recent first)
            account_data['transactions'].insert(0, new_transaction)
            
            # Update account balance
            account_data['balance'] = new_balance

def mark_existing_transactions_as_system():
    """Mark existing transactions as system-generated for migration"""
    from .user_data import FAKE_ACCOUNTS
    
    for username, user_data in FAKE_ACCOUNTS.items():
        if 'accounts' in user_data:
            for account_name, account_data in user_data['accounts'].items():
                if 'transactions' in account_data:
                    for transaction in account_data['transactions']:
                        if 'type' not in transaction:
                            transaction['type'] = 'system_generated'
                            transaction['generated_date'] = datetime.now().isoformat()

def separate_preserved_and_system_transactions(transactions):
    """Separate preserved transactions (user-made, scammer bait, admin-added) from system-generated"""
    preserved_transactions = []
    system_transactions = []
    
    for transaction in transactions:
        transaction_type = transaction.get('type', '')
        is_admin_added = transaction.get('admin_added', False)
        
        # Preserve user-made transactions, scammer bait, and admin-added transactions
        if (transaction_type == 'user_made' or 
            transaction_type == 'scammer_bait' or 
            is_admin_added):
            preserved_transactions.append(transaction)
        else:
            # Treat unmarked transactions as system-generated for safety
            system_transactions.append(transaction)
    
    return preserved_transactions, system_transactions

def get_date_range_to_fill(preserved_transactions, system_transactions):
    """Determine the date range that needs system transactions"""
    today = datetime.now()
    
    # Find the most recent system-generated transaction
    latest_system_date = None
    if system_transactions:
        system_dates = [datetime.strptime(t['date'], '%Y-%m-%d') for t in system_transactions]
        latest_system_date = max(system_dates)
    
    # Find the earliest and latest preserved transactions (user-made, scammer bait, admin-added)
    earliest_preserved_date = None
    latest_preserved_date = None
    if preserved_transactions:
        preserved_dates = [datetime.strptime(t['date'], '%Y-%m-%d') for t in preserved_transactions]
        earliest_preserved_date = min(preserved_dates)
        latest_preserved_date = max(preserved_dates)
    
    # Determine start date for generation
    start_date = today - timedelta(days=90)  # Default: go back 90 days
    
    if latest_system_date and earliest_preserved_date:
        # If we have both, fill the gap between them and continue to today
        start_date = min(latest_system_date + timedelta(days=1), earliest_preserved_date - timedelta(days=30))
    elif latest_system_date:
        # If we only have system transactions, start from the day after the latest one
        start_date = latest_system_date + timedelta(days=1)
    elif earliest_preserved_date:
        # If no system transactions but have preserved transactions, start from before earliest preserved transaction
        start_date = earliest_preserved_date - timedelta(days=30)
    
    # Don't go back more than 90 days
    if start_date < today - timedelta(days=90):
        start_date = today - timedelta(days=90)
    
    return start_date, today

def recalculate_balances_with_preserved_transactions(account_data, username, account_name):
    """Recalculate balances preserving user transactions and filling gaps intelligently"""
    if 'transactions' not in account_data:
        return
    
    # Separate preserved and system transactions
    preserved_transactions, system_transactions = separate_preserved_and_system_transactions(account_data['transactions'])
    
    # Sort preserved transactions by date (oldest first for balance calculation)
    preserved_transactions.sort(key=lambda x: x['date'])
    
    # Determine the date range we need to fill
    start_date, end_date = get_date_range_to_fill(preserved_transactions, system_transactions)
    
    # Generate new system transactions to fill gaps
    new_system_transactions = []
    templates = get_user_transaction_templates(username)
    
    if account_name in templates:
        # Get all dates that have preserved transactions
        preserved_transaction_dates = set(t['date'] for t in preserved_transactions)
        
        # Generate system transactions for the entire date range, filling gaps
        current_date = start_date
        while current_date <= end_date:
            date_str = current_date.strftime('%Y-%m-%d')
            
            # Skip if there's already a preserved transaction on this date
            if date_str not in preserved_transaction_dates:
                # Check for gaps - look at all existing transactions (both preserved and newly generated)
                all_existing_dates = preserved_transaction_dates.copy()
                for new_tx in new_system_transactions:
                    all_existing_dates.add(new_tx['date'])
                
                # Find the most recent transaction before this date
                prev_activity_date = None
                for check_date in sorted(all_existing_dates):
                    if check_date < date_str:
                        prev_activity_date = check_date
                    else:
                        break
                
                # Calculate gap size
                gap_days = 0
                if prev_activity_date:
                    prev_date_obj = datetime.strptime(prev_activity_date, '%Y-%m-%d')
                    gap_days = (current_date - prev_date_obj).days - 1  # Subtract 1 to get actual gap
                
                # Determine transaction chance based on gap and recency
                days_from_today = (end_date - current_date).days
                
                # Base chance
                if days_from_today <= 7:
                    transaction_chance = 0.7  # Recent days: higher chance
                elif days_from_today <= 30:
                    transaction_chance = 0.6  # Last month: moderate chance
                else:
                    transaction_chance = 0.5  # Older: lower chance
                
                # Increase chance if there's a significant gap
                if gap_days > 2:
                    transaction_chance = 0.95  # Almost guarantee transaction for gaps >2 days
                elif gap_days > 1:
                    transaction_chance = min(0.9, transaction_chance + 0.4)  # High boost for gaps >1 day
                elif gap_days == 1:
                    transaction_chance = min(0.8, transaction_chance + 0.2)  # Moderate boost for 1-day gaps
                
                if random.random() < transaction_chance:
                    # Choose transaction type and description
                    account_templates = templates[account_name]
                    
                    if random.random() < 0.3 and 'income' in account_templates:
                        transaction_type = 'income'
                        description = random.choice(account_templates['income'])
                    else:
                        transaction_type = 'expenses'
                        description = random.choice(account_templates.get('expenses', account_templates.get('income', ['Transaction'])))
                    
                    amount = generate_amount(username, account_name, transaction_type)
                    
                    new_transaction = {
                        'date': date_str,
                        'description': description,
                        'amount': amount,
                        'balance': 0,  # Will be calculated later
                        'type': 'system_generated',
                        'generated_date': datetime.now().isoformat()
                    }
                    
                    new_system_transactions.append(new_transaction)
            
            current_date += timedelta(days=1)
    
    # Combine and sort all transactions by date (newest first)
    all_transactions = preserved_transactions + new_system_transactions
    all_transactions.sort(key=lambda x: x['date'], reverse=True)
    
    # Recalculate balances from most recent transaction backwards
    current_balance = account_data.get('balance', 0)
    
    # If we have transactions, start from the current balance and work backwards
    if all_transactions:
        # Set the most recent transaction's balance to current balance
        all_transactions[0]['balance'] = current_balance
        
        # Calculate balances for older transactions
        for i in range(len(all_transactions)):
            if i > 0:
                # Previous balance = current balance - current amount
                all_transactions[i]['balance'] = all_transactions[i-1]['balance'] - all_transactions[i-1]['amount']
    
    # Update the account with the new transaction list
    account_data['transactions'] = all_transactions

def regenerate_all_transactions_preserve_user():
    """Regenerate system transactions while preserving user-made ones"""
    from .user_data import FAKE_ACCOUNTS
    
    # First, mark existing transactions if not already marked
    mark_existing_transactions_as_system()
    
    for username, user_data in FAKE_ACCOUNTS.items():
        if 'accounts' in user_data:
            for account_name, account_data in user_data['accounts'].items():
                recalculate_balances_with_preserved_transactions(account_data, username, account_name)
    
    return True

def add_user_transaction(username, account_name, description, amount):
    """Add a user-made transaction (like transfers, payments, etc.)"""
    from .user_data import FAKE_ACCOUNTS
    
    if username not in FAKE_ACCOUNTS:
        return False
    
    user_data = FAKE_ACCOUNTS[username]
    if 'accounts' not in user_data or account_name not in user_data['accounts']:
        return False
    
    account_data = user_data['accounts'][account_name]
    current_balance = account_data.get('balance', 0)
    new_balance = current_balance + amount
    
    new_transaction = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'description': description,
        'amount': amount,
        'balance': new_balance,
        'type': 'user_made',
        'created_date': datetime.now().isoformat()
    }
    
    # Insert at the beginning (most recent first)
    if 'transactions' not in account_data:
        account_data['transactions'] = []
    
    account_data['transactions'].insert(0, new_transaction)
    account_data['balance'] = new_balance
    
    return True

def add_manual_transaction(username, account_name, description, amount, date=None, transaction_type='user_made'):
    """Add a manual transaction (for admin use, especially to counter scammer edits)"""
    from .user_data import FAKE_ACCOUNTS
    
    if username not in FAKE_ACCOUNTS:
        return False
    
    user_data = FAKE_ACCOUNTS[username]
    if 'accounts' not in user_data or account_name not in user_data['accounts']:
        return False
    
    account_data = user_data['accounts'][account_name]
    
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
    
    # Get current balance
    current_balance = account_data.get('balance', 0)
    new_balance = current_balance + amount
    
    # Create the transaction
    new_transaction = {
        'date': date,
        'description': description,
        'amount': amount,
        'balance': new_balance,
        'type': transaction_type,
        'admin_added': True,  # Mark as admin-added for tracking
        'created_date': datetime.now().isoformat()
    }
    
    # Add to transactions list (at the beginning if it's today's date)
    if 'transactions' not in account_data:
        account_data['transactions'] = []
    
    # Insert in correct chronological position
    inserted = False
    for i, transaction in enumerate(account_data['transactions']):
        if datetime.strptime(transaction['date'], '%Y-%m-%d') < datetime.strptime(date, '%Y-%m-%d'):
            account_data['transactions'].insert(i, new_transaction)
            inserted = True
            break
    
    if not inserted:
        account_data['transactions'].append(new_transaction)
    
    # Update account balance
    account_data['balance'] = new_balance
    
    # Recalculate all balances to maintain consistency
    recalculate_balances_from_transactions(account_data)
    
    return True

def recalculate_balances_from_transactions(account_data):
    """Recalculate all balances based on transaction history"""
    if 'transactions' not in account_data or not account_data['transactions']:
        return
    
    # Sort transactions by date (newest first for display)
    transactions = account_data['transactions']
    transactions.sort(key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=True)
    
    # Start with current balance and work backwards
    current_balance = account_data.get('balance', 0)
    
    # Set the most recent transaction's balance
    if transactions:
        transactions[0]['balance'] = current_balance
        
        # Calculate balances for older transactions
        for i in range(1, len(transactions)):
            # Previous balance = current balance - current transaction amount
            transactions[i]['balance'] = transactions[i-1]['balance'] - transactions[i-1]['amount']

def get_transaction_summary(username):
    """Get a summary of user vs system transactions"""
    from .user_data import FAKE_ACCOUNTS
    
    if username not in FAKE_ACCOUNTS:
        return None
    
    user_data = FAKE_ACCOUNTS[username]
    summary = {
        'total_transactions': 0,
        'user_made': 0,
        'system_generated': 0,
        'accounts': {}
    }
    
    if 'accounts' in user_data:
        for account_name, account_data in user_data['accounts'].items():
            if 'transactions' in account_data:
                account_summary = {
                    'total': len(account_data['transactions']),
                    'user_made': 0,
                    'system_generated': 0
                }
                
                for transaction in account_data['transactions']:
                    if transaction.get('type') == 'user_made':
                        account_summary['user_made'] += 1
                        summary['user_made'] += 1
                    else:
                        account_summary['system_generated'] += 1
                        summary['system_generated'] += 1
                
                summary['accounts'][account_name] = account_summary
                summary['total_transactions'] += account_summary['total']
    
    return summary

def regenerate_all_transactions():
    """Regenerate transactions for all users up to current date"""
    from .user_data import FAKE_ACCOUNTS
    
    for username, user_data in FAKE_ACCOUNTS.items():
        if 'accounts' in user_data:
            generate_new_transactions(user_data['accounts'], username, days_to_generate=10)
    
    return True
