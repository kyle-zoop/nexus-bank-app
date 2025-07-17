# Modular Code Structure - Fake Bank Application

## 📁 Current File Organization

The fake bank application has been successfully modularized into separate files for better maintainability and code organization. Here's the complete structure:

### Core Application Files

#### 🎯 `app.py` - Main Flask Application
- **Purpose**: Main entry point and route definitions
- **Responsibilities**:
  - Flask app initialization
  - Route handlers (login, dashboard, transfer, etc.)
  - Template rendering
  - Session management
- **Dependencies**: Imports from all other modules
- **Key Routes**: `/`, `/login`, `/dashboard`, `/transfer`, `/statements`, `/support`, `/logout`

#### ⚙️ `config.py` - Configuration & Settings
- **Purpose**: Centralized configuration management
- **Contains**:
  - Flask settings (SECRET_KEY, DEBUG, PORT)
  - Security constants (BLACKLISTED_2FA_CODES, LOCKOUT_DURATION)
  - 2FA settings (MAX_2FA_ATTEMPTS, SESSION_2FA_TIMEOUT)
  - Processing delay settings (MIN_DELAY, MAX_DELAY)

#### 👥 `user_data.py` - User Account Data
- **Purpose**: All fake user account information
- **Contains**:
  - FAKE_ACCOUNTS dictionary with 5 user profiles:
    - `wealthy123` - Victoria Blackstone (Executive with $61M+ net worth)
    - `demo123` - John Anderson (Middle-class with multiple accounts)
    - `pooruser` - Sammy Broke (Basic user with minimal funds)
    - `retiree` - Evelyn Silver (Senior with retirement savings)
    - `student1` - Alex Undergrad (Student with loan debt)
  - Account types: checking, savings, credit cards, loans, investments
  - Transaction histories and balances

#### 🔐 `auth.py` - Security & Authentication
- **Purpose**: Security-related utilities
- **Functions**:
  - `is_account_locked()` - Check lockout status
  - `trigger_account_lockout()` - Lock account for 15 minutes
  - `is_blacklisted_code()` - Validate 2FA codes
  - `simulate_processing()` - Realistic delays
  - `get_2fa_method_message()` - 2FA notifications
- **Global State**: ACCOUNT_LOCKOUTS dictionary (per-user lockout tracking)

#### 🔄 `transfer_utils.py` - Transfer Processing
- **Purpose**: Banking transfer logic
- **Functions**:
  - `process_internal_transfer()` - Between user's accounts
  - `process_external_transfer()` - Fake external transfers
  - Balance validation and updates
  - Transaction history logging
  - Credit card payment handling

#### 🌐 `api_routes.py` - API Endpoints
- **Purpose**: RESTful API endpoints
- **Endpoints**:
  - `/api/balance` - Real-time balance data
  - `/api/verify_account` - Fake account verification
  - `/api/account_info/<type>` - Account details
- **Features**: JSON responses, authentication checks

### Template Files (UI)

#### 📄 Frontend Templates
- `templates/index.html` - Landing page
- `templates/login.html` - Login with 2FA support
- `templates/dashboard.html` - Main banking dashboard
- `templates/transfer.html` - Transfer interface
- `templates/statements.html` - Account statements
- `templates/support.html` - Customer support

#### 🎨 Static Assets
- `static/style.css` - Professional banking CSS
- Bootstrap 5 integration for responsive design

### Test Files

#### 🧪 Testing Suite
- `test_users.py` - User account validation
- `test_2fa_fix.py` - 2FA system testing
- `test_blacklist.py` - Blacklist code testing
- `test_lockout_independence.py` - Multi-user lockout testing
- `test_web_lockout.py` - Web interface lockout testing
- `test_transfers.py` - Transfer system testing
- `debug_lockout.py` - Lockout debugging utility

### Documentation

#### 📚 Documentation Files
- `README.md` - Main project documentation
- `DEVELOPMENT_SUMMARY.md` - Feature summary
- `2FA_IMPLEMENTATION.md` - 2FA system details
- `MODULAR_STRUCTURE.md` - This file

### Launch Scripts

#### 🚀 Startup Scripts
- `run_bank.bat` - Windows batch file launcher
- `run_bank.ps1` - PowerShell launcher script

## 🔧 Benefits of Modular Structure

### 1. **Separation of Concerns**
- Each module has a single, well-defined responsibility
- Easy to locate and modify specific functionality
- Reduced risk of unintended side effects

### 2. **Maintainability**
- Clear organization makes debugging easier
- Code changes are localized to relevant modules
- Easier onboarding for new developers

### 3. **Testability**
- Individual modules can be tested in isolation
- Mock dependencies easily for unit testing
- Clear interfaces between components

### 4. **Scalability**
- Easy to add new features without touching core logic
- Can extend user profiles in `user_data.py`
- API endpoints can be expanded in `api_routes.py`

### 5. **Configuration Management**
- All settings centralized in `config.py`
- Easy to adjust security parameters
- Environment-specific configurations possible

## 🔄 Import Dependencies

```
app.py
├── config.py (settings)
├── user_data.py (account data)
├── auth.py (security functions)
├── api_routes.py (API endpoints)
└── transfer_utils.py (transfer logic)

auth.py
└── config.py (security constants)

transfer_utils.py
└── (no dependencies - pure business logic)

api_routes.py
└── user_data.py (account access)
```

## 🎯 Future Enhancement Areas

### 1. **Database Integration**
- Replace in-memory `user_data.py` with database models
- Add data persistence layer
- Implement proper user registration

### 2. **Advanced Security**
- JWT token authentication
- Rate limiting per IP
- Enhanced session security

### 3. **Additional Modules**
- `notification_utils.py` - Email/SMS simulation
- `report_generator.py` - Account statements
- `admin_panel.py` - Administrative interface

### 4. **Testing Expansion**
- Unit tests for each module
- Integration tests for full workflows
- Performance testing

This modular structure provides a solid foundation for maintaining and expanding the fake bank application while keeping the codebase organized and professional.
