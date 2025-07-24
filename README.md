# Nexus Digital Bank - Scammer Honeypot

A realistic fake banking application designed for scammer engagement and security research.

## 🚀 Quick Start

### Development
```bash
python run_app.py
```
Visit: http://localhost:5000

### Production Deployment
See [DEPLOYMENT_GUIDE.md](docs/DEPLOYMENT_GUIDE.md) for detailed instructions.

## 📁 Project Structure

```
nexus-bank-app/
├── src/bank/           # Main application code
├── tests/              # Test files
├── scripts/            # Utility scripts
├── docs/               # Documentation
├── requirements.txt    # Python dependencies
├── Procfile           # Deployment configuration
├── runtime.txt        # Python version for deployment
└── run_app.py         # Application entry point
```

## ✨ Features

- **Realistic Banking Interface**: Professional UI that convinces scammers
- **Enhanced 2FA Security**: All invalid codes trigger account lockouts
- **Admin Panel**: Separate interface for monitoring activity
- **Account Lockout System**: 15-minute lockouts with visual countdown
- **Transaction History**: Fake transaction data to engage scammers
- **Transfer System**: Fake money transfer functionality
- **Statement Generation**: Realistic bank statements

## 🔒 Security Features

- Session-based authentication
- TOTP 2FA simulation
- Account lockout protection
- Admin/user isolation
- Production-ready configuration

## 📊 User Accounts

### Regular Users (for scammers)
- **vhamilton**: Wealthy target account ($2.8M balance)
- **janderson47**: High-value account ($890K balance)
- **mwilson**: Mid-range account ($45K balance)

### Admin Access
- **admin**: Administrative interface for monitoring

*See [user_data.py](src/bank/user_data.py) for complete account details*

## 🎯 Purpose

This application is designed for:
- Cybersecurity research
- Scammer engagement and time-wasting
- Educational purposes on social engineering tactics

## ⚠️ Legal Notice

This software is for educational and research purposes only. Users are responsible for complying with all applicable laws and regulations in their jurisdiction.

## 📚 Documentation

- [Admin Guide](docs/ADMIN_GUIDE.md) - Administrative features
- [Deployment Guide](docs/DEPLOYMENT_GUIDE.md) - Production deployment
- [Security System](docs/2FA_SECURITY_SYSTEM.md) - 2FA implementation details

## 🔧 Development

### Requirements
- Python 3.11+
- Flask and dependencies (see requirements.txt)

### Testing
```bash
python -m pytest tests/
```

## 📄 License

MIT License - See LICENSE file for details.
