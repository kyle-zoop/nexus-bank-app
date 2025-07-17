# Global Trust Bank - Fake Bank for Scam Baiting

A realistic fake bank website designed for educational purposes and scam baiting. This application mimics the interface and functionality of a real banking website to waste scammers' time and expose their tactics.

## ⚠️ IMPORTANT DISCLAIMER

This is a **FAKE BANK** designed for:
- Educational purposes
- Scam baiting activities
- Demonstrating phishing awareness
- Testing and research

**DO NOT USE FOR:**
- Actual financial transactions
- Deception of legitimate users
- Illegal activities
- Real financial services

## Features

### Realistic Banking Interface
- Professional bank homepage with trust indicators
- Secure login system (demo credentials provided)
- Account dashboard with realistic balance and transactions
- Money transfer functionality with validation
- Account statements and transaction history
- 24/7 customer support chat system
- Security alerts and notifications

### Built for Scam Baiting
- Realistic delays and processing times
- Fake account verification systems
- Professional-looking statements and confirmations
- Customer support responses
- Security badges and trust indicators
- FDIC and regulatory mentions

### Demo Account
- **Username:** `demo123`
- **Password:** `secure456`
- **Account Balance:** $2,847,563.89
- **Account Type:** Premium Savings

## Quick Start

1. **Install Python Dependencies:**
   ```powershell
   cd "c:\Projects\bank"
   pip install -r requirements.txt
   ```

2. **Run the Application:**
   ```powershell
   python app.py
   ```

3. **Access the Bank:**
   Open your web browser and navigate to: `http://localhost:5000`

4. **Login with Demo Account:**
   - Username: `demo123`
   - Password: `secure456`

## File Structure

```
bank/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── static/
│   ├── style.css         # Custom bank styling
│   └── script.js         # Interactive functionality
└── templates/
    ├── base.html         # Base template
    ├── index.html        # Homepage
    ├── login.html        # Login page
    ├── dashboard.html    # Account dashboard
    ├── transfer.html     # Money transfer
    ├── statements.html   # Account statements
    └── support.html      # Customer support
```

## Key Features for Scam Baiting

### 1. Realistic User Interface
- Professional banking design using Bootstrap
- Trust indicators (FDIC, SSL certificates, etc.)
- Security badges and encryption notices
- Real-time notifications and alerts

### 2. Convincing Functionality
- Account balance and transaction history
- Wire transfer forms with validation
- Statement downloads (fake documents)
- Customer support chat with auto-responses
- Account verification processes

### 3. Time-Wasting Elements
- Processing delays for all actions
- Multi-step verification processes
- Customer service chat that leads nowhere
- Form validations that always "succeed"
- Email confirmations that never arrive

### 4. Professional Details
- Realistic account numbers and routing numbers
- SWIFT codes for international transfers
- Professional customer service responses
- Banking terminology and procedures
- Security warnings and fraud alerts

## Usage Tips for Scam Baiting

1. **Share Login Credentials Carefully:**
   - Only give fake credentials to scammers
   - Monitor who attempts to access the system

2. **Use Realistic Delays:**
   - The system includes built-in delays to waste scammers' time
   - Transfer "processing" can take several fake business days

3. **Customer Support Responses:**
   - The chat system provides realistic but unhelpful responses
   - Perfect for keeping scammers engaged

4. **Documentation:**
   - Save screenshots of scammer interactions
   - Use the fake statements as "proof" of funds

## Customization

### Adding More Fake Accounts
Edit the `FAKE_ACCOUNTS` dictionary in `app.py`:

```python
FAKE_ACCOUNTS = {
    'username': {
        'password': 'password',
        'name': 'Account Holder Name',
        'account_number': '1234-5678-9012-3456',
        'balance': 1000000.00,
        # ... other details
    }
}
```

### Modifying Bank Information
Update the bank details in the templates:
- Bank name: "Global Trust Bank"
- Phone numbers: 1-800-TRUST-1
- SWIFT code: CBKDUS33XXX
- Routing number: 021000021

### Adding More Realistic Features
- Modify transaction history in the account data
- Add more customer support responses
- Include additional form validation
- Add more fake statements and documents

## Security Notes

- This application runs locally and doesn't connect to real banking systems
- No real financial data is processed
- All account information is completely fictional
- The application includes no actual security measures

## Legal Considerations

- Use only for legitimate scam baiting and educational purposes
- Do not use to deceive innocent individuals
- Ensure compliance with local laws regarding fake websites
- Document scammer interactions for potential law enforcement

## Technical Details

- **Framework:** Flask (Python)
- **Frontend:** Bootstrap 5, Font Awesome icons
- **Database:** None (all data is in-memory)
- **Security:** Basic session management (not production-ready)

## Troubleshooting

### Common Issues
1. **Port 5000 already in use:**
   ```python
   app.run(debug=True, port=5001)  # Use different port
   ```

2. **Templates not loading:**
   - Ensure templates folder exists
   - Check file permissions

3. **Static files not loading:**
   - Verify static folder structure
   - Check CSS/JS file paths

## Contributing

This is a specialized tool for scam baiting. If you want to improve it:
- Add more realistic banking features
- Improve the user interface
- Add more time-wasting elements
- Enhance the customer support responses

## Disclaimer

This software is provided "as is" for educational and scam baiting purposes only. The creators are not responsible for any misuse of this application. Always ensure your scam baiting activities comply with local laws and regulations.

---

**Remember: This is a FAKE BANK. Never use it to deceive legitimate users or for illegal activities.**

## Multi-Account and Balance Refresh Features

### Multi-Account Support
- **Checking Account** - Primary transactional account with realistic balance
- **Savings Account** - High-yield savings with substantial balance for scammer interest
- **Credit Card** - Platinum rewards card with available credit and payment functionality
- **Mortgage Account** - Home loan with monthly payment tracking
- **Investment Portfolio** - Investment account with YTD returns and portfolio value
- **Auto Loan** - Vehicle financing with payment schedule

### Transfer System
- **Internal Transfers** - Move money between user's own accounts
- **External Transfers** - Wire transfers (domestic/international/ACH) with fake processing
- **Real-time Balance Updates** - Live balance refresh after transfers
- **Transfer Confirmations** - Realistic confirmation IDs and processing times
- **Credit Card Payments** - Pay credit card balances from other accounts

### Dashboard Features
- **Real-time Balance Refresh** - Click refresh button to update all account balances
- **Auto-refresh** - Balances automatically update every 60 seconds when page is active
- **Post-transfer Updates** - Dashboard automatically refreshes after successful transfers
- **Multi-account Overview** - All account types displayed with appropriate styling and information

### Two-Factor Authentication (2FA)
- **SMS Verification** - 6-digit codes sent via SMS (simulated)
- **Email Verification** - Codes sent to registered email (simulated)
- **Authenticator App** - Support for app-based 2FA (simulated)
- **Security Features** - 3 attempt limit, 5-minute code expiry
- **Realistic Flow** - Multi-step login process with proper validation
- **Demo Codes** - For testing, 2FA codes are displayed in flash messages

### Enhanced Security Features
- **Session Management** - Secure session handling with timeouts
- **Attempt Limiting** - Automatic lockout after failed attempts
- **Code Expiry** - Time-limited verification codes
- **SSL Indicators** - Visual security indicators on login page
- **Device Recognition** - "Remember this device" option (simulated)
