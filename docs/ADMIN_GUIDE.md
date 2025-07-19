# Admin Panel Documentation

## Overview
The Nexus Bank Admin Panel provides system management capabilities for maintaining realistic fake bank data.

## Access
- **URL**: `/admin`
- **Default Password**: `admin123`
- **Environment Variable**: Set `ADMIN_PASSWORD` to change the default password

## Features

### 🔄 Transaction Management
- **Regenerate Recent Transactions**: Adds realistic transactions for the past 10 days to keep data current
- **Clear Old Transactions**: Removes transactions older than 6 months to keep the database clean

### 🔐 Security Management
- **Clear All Account Lockouts**: Resets all account lockout states
- **Reset 2FA Attempts**: Clears all failed 2FA attempt counters

### 📊 System Statistics
- Total number of users and accounts
- Total transaction count
- Last data update timestamp
- Current system time and debug status

## Usage

### Keeping Data Current
The most important feature is the transaction regeneration. This should be run periodically to:
- Add realistic new transactions up to the current date
- Maintain the illusion of an active, real bank account
- Keep balance changes realistic and believable

### Automated Updates
You can also use the standalone script:
```bash
python update_transactions.py
```

### Scheduled Tasks
For production use, consider setting up a scheduled task to run transaction updates:

**Windows (Task Scheduler)**:
- Schedule `python update_transactions.py` to run daily

**Linux/Mac (Cron)**:
```bash
0 2 * * * cd /path/to/nexus-bank-app && python update_transactions.py
```

## Security Notes
- The admin panel uses a simple password authentication
- For production use, implement proper admin user management
- Consider restricting access by IP address
- The admin session persists until browser closure

## Transaction Generation
The system generates transactions based on user profiles:
- **Wealthy users**: Large investments, luxury purchases, high-value transactions
- **Middle class**: Regular expenses, payroll, moderate spending
- **Poor users**: Small purchases, part-time income, limited transactions
- **Retirees**: Pension deposits, senior-appropriate expenses
- **Students**: Part-time work, small purchases, educational expenses

Each transaction type has realistic amount ranges and descriptions appropriate to the user's financial situation.
