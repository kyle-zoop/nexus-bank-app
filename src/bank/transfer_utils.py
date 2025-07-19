"""
Transfer processing utilities for the fake bank application
"""
import uuid
from datetime import datetime
from flask import flash

def process_internal_transfer(user_data, from_account, to_account, amount):
    """Process internal transfer between user's accounts"""
    if from_account == to_account:
        flash('Cannot transfer to the same account.', 'error')
        return False
    
    source_account = user_data['accounts'][from_account]
    dest_account = user_data['accounts'][to_account]
    
    # Check if source account has sufficient funds
    if from_account == 'credit_card':
        if amount > source_account['available_credit']:
            flash('Insufficient available credit for this transfer.', 'error')
            return False
    else:
        if amount > source_account['balance']:
            flash('Insufficient funds in source account.', 'error')
            return False
    
    # Perform the transfer
    if from_account == 'credit_card':
        # Transfer FROM credit card (cash advance): increase debt, decrease available credit
        source_account['balance'] -= amount  # More negative (more debt)
        source_account['available_credit'] -= amount
        dest_account['balance'] += amount
    elif to_account == 'credit_card':
        # Transfer TO credit card (payment): decrease debt, increase available credit
        source_account['balance'] -= amount
        dest_account['balance'] += amount  # Less negative (less debt)
        dest_account['available_credit'] += amount
    else:
        # Regular account to account transfer
        source_account['balance'] -= amount
        dest_account['balance'] += amount
    
    # Update available balances for investment accounts
    if 'available_balance' in source_account:
        source_account['available_balance'] = source_account['balance']
    if 'available_balance' in dest_account:
        dest_account['available_balance'] = dest_account['balance']
    
    # Add transaction records to both accounts
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Add transaction to source account
    source_transaction = {
        'date': today,
        'description': f'Transfer to {dest_account["account_type"]}',
        'amount': -amount,
        'balance': source_account['balance'],
        'type': 'user_made',
        'created_date': datetime.now().isoformat()
    }
    source_account['transactions'].insert(0, source_transaction)
    
    # Add transaction to destination account
    dest_transaction = {
        'date': today,
        'description': f'Transfer from {source_account["account_type"]}',
        'amount': amount,
        'balance': dest_account['balance'],
        'type': 'user_made',
        'created_date': datetime.now().isoformat()
    }
    dest_account['transactions'].insert(0, dest_transaction)
    
    # Keep only last 10 transactions for each account
    source_account['transactions'] = source_account['transactions'][:10]
    dest_account['transactions'] = dest_account['transactions'][:10]
    
    confirmation_id = str(uuid.uuid4())[:8].upper()
    try:
        flash(f'Internal transfer of ${amount:,.2f} completed successfully! Confirmation ID: {confirmation_id}', 'success')
        flash(f'Transferred from {source_account["account_type"]} to {dest_account["account_type"]}', 'info')
    except RuntimeError:
        # Working outside request context (testing mode)
        pass
    
    return True

def process_external_transfer(user_data, from_account, amount, recipient, transfer_type):
    """Process external transfer to another bank"""
    if not from_account:
        return False
    
    source_account = user_data['accounts'][from_account]
    
    # Check source account has sufficient funds
    if from_account == 'credit_card':
        if amount > source_account['available_credit']:
            flash('Insufficient available credit for this transfer.', 'error')
            return False
    else:
        if amount > source_account['balance']:
            flash('Insufficient funds in source account.', 'error')
            return False
    
    # For external transfers, just deduct from source account (fake transfer)
    if from_account == 'credit_card':
        source_account['balance'] -= amount
        source_account['available_credit'] -= amount
    else:
        source_account['balance'] -= amount
    
    # Add transaction record
    today = datetime.now().strftime('%Y-%m-%d')
    
    transfer_description = f'{transfer_type.title()} Wire Transfer to {recipient}'
    source_transaction = {
        'date': today,
        'description': transfer_description,
        'amount': -amount,
        'balance': source_account['balance'],
        'type': 'user_made',
        'created_date': datetime.now().isoformat()
    }
    source_account['transactions'].insert(0, source_transaction)
    source_account['transactions'] = source_account['transactions'][:10]
    
    confirmation_id = str(uuid.uuid4())[:8].upper()
    processing_time = {
        'ach': '1-3 business days',
        'domestic': 'same day',
        'international': '1-5 business days'
    }
    
    try:
        flash(f'{transfer_type.title()} transfer of ${amount:,.2f} initiated. Confirmation ID: {confirmation_id}', 'success')
        flash(f'Transfer to {recipient} is being processed and may take {processing_time[transfer_type]}.', 'info')
    except RuntimeError:
        # Working outside request context (testing mode)
        pass
    
    return True
