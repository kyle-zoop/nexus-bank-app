"""
User account data for the fake bank application
Multiple identities for scam baiting scenarios with extensive transaction history
"""

FAKE_ACCOUNTS = {
    # Wealthy user
    'vhamilton': {
        'password': 'VictoriaH@123',
        'name': 'Victoria Hamilton',
        'email': 'v.hamilton@execpartners.com',
        'phone': '+61 2 9876 5432',
        'routing_number': '062-692',
        'swift_code': 'NEXAAU2SXXX',
        '2fa_enabled': True,
        '2fa_method': 'app',
        '2fa_phone': '***-***-5432',
        'accounts': {
            'checking': {
                'account_number': '4029-8765-4728-3915',
                'account_type': 'Executive Platinum Checking',
                'balance': 4271345.34,
                'transactions': [
                    {'date': '2025-07-10', 'description': 'Executive Salary Deposit', 'amount': 187271.00, 'balance': 4271345.34},
                    {'date': '2025-07-09', 'description': 'Private Jet Charter', 'amount': -70858.00, 'balance': 4084074.34},
                    {'date': '2025-07-05', 'description': 'Royal Melbourne Golf Club', 'amount': -13124.25, 'balance': 4154932.34},
                    {'date': '2025-06-28', 'description': 'Executive Salary Deposit', 'amount': 187271.00, 'balance': 4168056.59},
                    {'date': '2025-06-25', 'description': 'Aston Martin Purchase', 'amount': -281189.75, 'balance': 3980785.59},
                    {'date': '2025-06-20', 'description': 'Investment Dividend', 'amount': 112338.23, 'balance': 4262975.34},
                    {'date': '2025-06-15', 'description': 'Art Auction - Sotheby\'s', 'amount': -372956.94, 'balance': 4150637.11},
                    {'date': '2025-05-30', 'description': 'Executive Salary Deposit', 'amount': 187271.00, 'balance': 4523594.05},
                    {'date': '2025-05-22', 'description': 'Yacht Maintenance - Marina', 'amount': -52313.91, 'balance': 4336323.05},
                    {'date': '2025-05-18', 'description': 'Private School Fees', 'amount': -67424.60, 'balance': 4388637.96},
                    {'date': '2025-04-28', 'description': 'Executive Salary Deposit', 'amount': 187271.00, 'balance': 4456062.56},
                    {'date': '2025-04-15', 'description': 'Gold Coast Holiday', 'amount': -117951.41, 'balance': 4388637.96},
                    {'date': '2025-03-30', 'description': 'Executive Salary Deposit', 'amount': 187271.00, 'balance': 4378589.37},
                    {'date': '2025-03-12', 'description': 'Red Cross Gala Donation', 'amount': -74195.73, 'balance': 4191318.37},
                    {'date': '2025-02-28', 'description': 'Executive Salary Deposit', 'amount': 187271.00, 'balance': 4265514.10},
                    {'date': '2025-02-14', 'description': 'Tiffany & Co Sydney', 'amount': -126413.85, 'balance': 4078243.10},
                    {'date': '2025-01-31', 'description': 'Executive Salary Deposit', 'amount': 187271.00, 'balance': 4204656.95},
                    {'date': '2024-12-31', 'description': 'Year-End Bonus', 'amount': 730987.01, 'balance': 4017385.95},
                    {'date': '2024-12-15', 'description': 'Christmas Shopping - Melbourne', 'amount': -185534.16, 'balance': 3286398.94},
                    {'date': '2024-11-28', 'description': 'Executive Salary Deposit', 'amount': 187271.00, 'balance': 3471933.10}
                ]
            },
            'savings': {
                'account_number': '4029-8765-8293-7641',
                'account_type': 'Private Wealth Savings',
                'balance': 15847563.89,
                'transactions': [
                    {'date': '2025-07-10', 'description': 'Bond Interest Payment', 'amount': 245000.00, 'balance': 15847563.89},
                    {'date': '2025-07-01', 'description': 'Monthly Interest Compound', 'amount': 158475.64, 'balance': 15602563.89},
                    {'date': '2025-06-15', 'description': 'Treasury Bill Maturation', 'amount': 500000.00, 'balance': 15444088.25},
                    {'date': '2025-06-01', 'description': 'Monthly Interest Compound', 'amount': 154440.88, 'balance': 14944088.25},
                    {'date': '2025-05-20', 'description': 'CD Rollover Deposit', 'amount': 1000000.00, 'balance': 14789647.37},
                    {'date': '2025-05-01', 'description': 'Monthly Interest Compound', 'amount': 147896.47, 'balance': 13789647.37},
                    {'date': '2025-04-10', 'description': 'Investment Transfer In', 'amount': 2500000.00, 'balance': 13641750.90},
                    {'date': '2025-04-01', 'description': 'Monthly Interest Compound', 'amount': 114175.09, 'balance': 11141750.90},
                    {'date': '2025-03-15', 'description': 'Quarterly Dividend Reinvest', 'amount': 850000.00, 'balance': 11027575.81},
                    {'date': '2025-03-01', 'description': 'Monthly Interest Compound', 'amount': 101775.76, 'balance': 10177575.81},
                    {'date': '2025-02-01', 'description': 'Monthly Interest Compound', 'amount': 100758.00, 'balance': 10075800.05},
                    {'date': '2025-01-15', 'description': 'Year-End Rollover', 'amount': 500000.00, 'balance': 9975042.05},
                    {'date': '2025-01-01', 'description': 'Monthly Interest Compound', 'amount': 99750.42, 'balance': 9475042.05},
                    {'date': '2024-12-15', 'description': 'Holiday Bonus Deposit', 'amount': 1000000.00, 'balance': 9375291.63},
                    {'date': '2024-12-01', 'description': 'Monthly Interest Compound', 'amount': 93752.92, 'balance': 8375291.63}
                ]
            },
            'credit_card': {
                'account_number': '4532-PLAT-5678-9012',
                'account_type': 'Black Card - Unlimited',
                'balance': -89547.92,
                'available_credit': 4910452.08,
                'credit_limit': 5000000.00,
                'min_payment': 2486.73,
                'transactions': [
                    {'date': '2025-07-10', 'description': 'Luxury Resort - Gold Coast', 'amount': -28934.56, 'balance': -89547.92},
                    {'date': '2025-07-08', 'description': 'Private Shopping Session', 'amount': -15000.00, 'balance': -60613.36},
                    {'date': '2025-07-05', 'description': 'Fine Dining - Attica Melbourne', 'amount': -2850.00, 'balance': -45613.36},
                    {'date': '2025-07-01', 'description': 'Payment Received', 'amount': 125000.00, 'balance': -42763.36},
                    {'date': '2025-06-28', 'description': 'Helicopter Charter', 'amount': -8500.00, 'balance': -167763.36},
                    {'date': '2025-06-25', 'description': 'Designer Handbag Collection', 'amount': -45000.00, 'balance': -159263.36},
                    {'date': '2025-06-20', 'description': 'Spa Weekend Package', 'amount': -12500.00, 'balance': -114263.36},
                    {'date': '2025-06-15', 'description': 'Wine Auction Purchase', 'amount': -35000.00, 'balance': -101763.36},
                    {'date': '2025-06-01', 'description': 'Payment Received', 'amount': 150000.00, 'balance': -66763.36},
                    {'date': '2025-05-28', 'description': 'Luxury Watch Purchase', 'amount': -95000.00, 'balance': -216763.36},
                    {'date': '2025-05-22', 'description': 'Private Jet Catering', 'amount': -5500.00, 'balance': -121763.36},
                    {'date': '2025-05-18', 'description': 'Art Gallery Purchase', 'amount': -78000.00, 'balance': -116263.36},
                    {'date': '2025-05-01', 'description': 'Payment Received', 'amount': 200000.00, 'balance': -38263.36},
                    {'date': '2025-04-25', 'description': 'Crown Casino Melbourne', 'amount': -125000.00, 'balance': -238263.36},
                    {'date': '2025-04-20', 'description': 'Yacht Club Membership', 'amount': -25000.00, 'balance': -113263.36}
                ]
            },
            'mortgage': {
                'account_number': '4029-8765-5739-8264',
                'account_type': 'Luxury Estate Mortgage',
                'balance': -2450000.00,
                'monthly_payment': 18247.92,
                'interest_rate': 2.95,
                'term_remaining': '12 years, 8 months',
                'next_payment_date': '2025-08-01',
                'property_address': '1 Sovereign Place, Toorak, VIC 3142',
                'transactions': [
                    {'date': '2025-07-01', 'description': 'Monthly Payment Received', 'amount': 18247.92, 'balance': -2450000.00},
                ]
            },
            'investment': {
                'account_number': '4029-8765-9148-5027',
                'account_type': 'Private Investment Portfolio',
                'balance': 45670890.45,
                'available_balance': 45670890.45,
                'ytd_return': 28.4,
                'transactions': [
                    {'date': '2025-07-10', 'description': 'Tesla Stock Gains', 'amount': 2456789.12, 'balance': 45670890.45},
                    {'date': '2025-07-09', 'description': 'Tech Fund Distribution', 'amount': 889743.67, 'balance': 43214101.33},
                    {'date': '2025-07-05', 'description': 'NVIDIA Stock Split Bonus', 'amount': 1249284.15, 'balance': 42324357.66},
                    {'date': '2025-06-30', 'description': 'Quarterly Rebalancing', 'amount': -499837.92, 'balance': 41075073.51},
                    {'date': '2025-06-28', 'description': 'Amazon Stock Appreciation', 'amount': 1798642.33, 'balance': 41574101.33},
                    {'date': '2025-06-20', 'description': 'Crypto Portfolio Gains', 'amount': 749187.84, 'balance': 39775459.00},
                    {'date': '2025-06-15', 'description': 'Real Estate REIT Dividend', 'amount': 419593.66, 'balance': 39026271.16},
                    {'date': '2025-06-01', 'description': 'Monthly Portfolio Review', 'amount': 0.00, 'balance': 38604101.33},
                    {'date': '2025-05-25', 'description': 'Apple Stock Dividend', 'amount': 325000.00, 'balance': 38604101.33},
                    {'date': '2025-05-20', 'description': 'Hedge Fund Performance', 'amount': 2100000.00, 'balance': 38279101.33},
                    {'date': '2025-05-15', 'description': 'Microsoft Stock Gains', 'amount': 980000.00, 'balance': 36179101.33},
                    {'date': '2025-05-01', 'description': 'Gold Futures Profit', 'amount': 650000.00, 'balance': 35199101.33},
                    {'date': '2025-04-25', 'description': 'Private Equity Distribution', 'amount': 1500000.00, 'balance': 34549101.33},
                    {'date': '2025-04-15', 'description': 'Bond Portfolio Interest', 'amount': 385000.00, 'balance': 33049101.33},
                    {'date': '2025-04-01', 'description': 'Q1 Performance Bonus', 'amount': 2250000.00, 'balance': 32664101.33},
                    {'date': '2025-03-20', 'description': 'Energy Sector Rally', 'amount': 1100000.00, 'balance': 30414101.33},
                    {'date': '2025-03-01', 'description': 'International Fund Growth', 'amount': 875000.00, 'balance': 29314101.33},
                    {'date': '2025-02-15', 'description': 'Tech Stock Surge', 'amount': 1950000.00, 'balance': 28439101.33},
                    {'date': '2025-01-31', 'description': 'Year-End Rebalancing', 'amount': 500000.00, 'balance': 26489101.33},
                    {'date': '2024-12-31', 'description': 'Annual Performance Review', 'amount': 3500000.00, 'balance': 25989101.33}
                ]
            }
        }
    },
    
    # Middle class user
    'jcarter1973': {
        'password': 'carter1973!',
        'name': 'James Carter',
        'email': 'jamesWcarter1973@gmail.com',
        'phone': '+61 3 1234 5678',
        'routing_number': '062-692',
        'swift_code': 'NEXAAU2SXXX',
        '2fa_enabled': True,
        '2fa_method': 'sms',
        '2fa_phone': '***-***-4567',
        'accounts': {
            'checking': {
                'account_number': '4029-8765-3847-6592',
                'account_type': 'Everyday Checking',
                'balance': 2313.02,
                'transactions': [
                    {'date': '2025-07-10', 'description': 'Payroll Deposit', 'amount': 3730.99, 'balance': 2313.02},
                    {'date': '2025-07-09', 'description': 'Woolworths', 'amount': -185.18, 'balance': -1418.97},
                    {'date': '2025-07-08', 'description': 'BP Service Station', 'amount': -97.17, 'balance': -1233.79},
                    {'date': '2025-07-05', 'description': 'Origin Energy Bill', 'amount': -218.25, 'balance': -1136.62},
                    {'date': '2025-07-03', 'description': 'ATM Withdrawal', 'amount': -120.00, 'balance': -918.37},
                    {'date': '2025-07-01', 'description': 'Rent Payment', 'amount': -1792.23, 'balance': -798.37},
                    {'date': '2025-06-26', 'description': 'Payroll Deposit', 'amount': 3730.99, 'balance': 993.86},
                    {'date': '2025-06-24', 'description': 'Restaurant - Date Night', 'amount': -128.25, 'balance': -2739.13},
                    {'date': '2025-06-22', 'description': 'Coles Supermarket', 'amount': -202.20, 'balance': -2610.88},
                    {'date': '2025-06-20', 'description': 'Shell Service Station', 'amount': -88.13, 'balance': -2408.68},
                    {'date': '2025-06-18', 'description': 'Coffee Shop', 'amount': -12.50, 'balance': -1543.67},
                    {'date': '2025-06-15', 'description': 'Internet Bill', 'amount': -89.99, 'balance': -1531.17},
                    {'date': '2025-06-12', 'description': 'Payroll Deposit', 'amount': 2487.33, 'balance': -1441.18},
                    {'date': '2025-06-10', 'description': 'Phone Bill', 'amount': -74.95, 'balance': -3941.18},
                    {'date': '2025-06-08', 'description': 'Grocery Store', 'amount': -145.20, 'balance': -3866.18},
                    {'date': '2025-06-05', 'description': 'Medical Co-pay', 'amount': -34.67, 'balance': -3720.98},
                    {'date': '2025-06-01', 'description': 'Rent Payment', 'amount': -1194.82, 'balance': -3685.98},
                    {'date': '2025-05-28', 'description': 'Payroll Deposit', 'amount': 2487.33, 'balance': -2485.98},
                    {'date': '2025-05-25', 'description': 'Birthday Gift Shopping', 'amount': -126.73, 'balance': -4985.98},
                    {'date': '2025-05-20', 'description': 'Grocery Store', 'amount': -167.45, 'balance': -4860.98}
                ]
            },
            'savings': {
                'account_number': '4029-8765-7265-4918',
                'account_type': 'Standard Savings',
                'balance': 3200.00,
                'transactions': [
                    {'date': '2025-07-10', 'description': 'Interest Payment', 'amount': 1.25, 'balance': 3200.00},
                    {'date': '2025-07-01', 'description': 'Monthly Savings Transfer', 'amount': 199.73, 'balance': 3198.75},
                    {'date': '2025-06-10', 'description': 'Interest Payment', 'amount': 1.20, 'balance': 2999.02},
                    {'date': '2025-06-01', 'description': 'Monthly Savings Transfer', 'amount': 199.73, 'balance': 2997.82},
                    {'date': '2025-05-25', 'description': 'Emergency Fund Withdrawal', 'amount': -497.84, 'balance': 2797.82},
                    {'date': '2025-05-10', 'description': 'Interest Payment', 'amount': 1.32, 'balance': 3295.66},
                    {'date': '2025-05-01', 'description': 'Monthly Savings Transfer', 'amount': 199.73, 'balance': 3294.34},
                    {'date': '2025-04-10', 'description': 'Interest Payment', 'amount': 1.25, 'balance': 3096.23},
                    {'date': '2025-04-01', 'description': 'Monthly Savings Transfer', 'amount': 200.00, 'balance': 3094.98},
                    {'date': '2025-03-15', 'description': 'Tax Refund Deposit', 'amount': 847.29, 'balance': 2894.98},
                    {'date': '2025-03-10', 'description': 'Interest Payment', 'amount': 1.02, 'balance': 2047.69},
                    {'date': '2025-03-01', 'description': 'Monthly Savings Transfer', 'amount': 199.73, 'balance': 2046.67},
                    {'date': '2025-02-10', 'description': 'Interest Payment', 'amount': 0.92, 'balance': 1843.96},
                    {'date': '2025-02-01', 'description': 'Monthly Savings Transfer', 'amount': 200.00, 'balance': 1843.04},
                    {'date': '2025-01-10', 'description': 'Interest Payment', 'amount': 0.82, 'balance': 1643.04}
                ]
            },
            'auto_loan': {
                'account_number': '4029-8765-6483-2057',
                'account_type': 'Auto Loan - 2024 BMW X5',
                'balance': -23456.78,
                'monthly_payment': 687.45,
                'interest_rate': 4.9,
                'term_remaining': '2 years, 8 months',
                'next_payment_date': '2025-07-25',
                'transactions': [
                    {'date': '2025-06-25', 'description': 'Monthly Payment Received', 'amount': 687.45, 'balance': -23456.78},
                    {'date': '2025-05-25', 'description': 'Monthly Payment Received', 'amount': 687.45, 'balance': -24144.23},
                    {'date': '2025-04-25', 'description': 'Monthly Payment Received', 'amount': 687.45, 'balance': -24831.68},
                    {'date': '2025-03-25', 'description': 'Monthly Payment Received', 'amount': 687.45, 'balance': -25519.13},
                    {'date': '2025-02-25', 'description': 'Monthly Payment Received', 'amount': 687.45, 'balance': -26206.58},
                    {'date': '2025-01-25', 'description': 'Monthly Payment Received', 'amount': 687.45, 'balance': -26894.03},
                    {'date': '2024-12-25', 'description': 'Monthly Payment Received', 'amount': 687.45, 'balance': -27581.48},
                    {'date': '2024-11-25', 'description': 'Monthly Payment Received', 'amount': 687.45, 'balance': -28268.93},
                    {'date': '2024-10-25', 'description': 'Monthly Payment Received', 'amount': 687.45, 'balance': -28956.38},
                    {'date': '2024-09-25', 'description': 'Monthly Payment Received', 'amount': 687.45, 'balance': -29643.83},
                    {'date': '2024-08-25', 'description': 'Monthly Payment Received', 'amount': 687.45, 'balance': -30331.28},
                    {'date': '2024-07-25', 'description': 'Monthly Payment Received', 'amount': 687.45, 'balance': -31018.73},
                    {'date': '2024-06-25', 'description': 'Monthly Payment Received', 'amount': 687.45, 'balance': -31706.18},
                    {'date': '2024-05-25', 'description': 'Monthly Payment Received', 'amount': 687.45, 'balance': -32393.63},
                    {'date': '2024-04-15', 'description': 'Loan Origination - BMW X5', 'amount': -45000.00, 'balance': -33081.08}
                ]
            }
        }
    },
    
    # Poor user
    'sbrooks85': {
        'password': 'SamuelB85!',
        'name': 'Samuel Brooks',
        'email': 'samuelbrooks85@yahoo.com',
        'phone': '+61 7 0000 0005',
        'routing_number': '062-692',
        'swift_code': 'NEXAAU2SXXX',
        '2fa_enabled': True,
        '2fa_method': 'sms',
        '2fa_phone': '***-***-0005',
        'accounts': {
            'checking': {
                'account_number': '4029-8765-1947-8352',
                'account_type': 'Basic Checking',
                'balance': 5.00,
                'transactions': [
                    {'date': '2025-07-10', 'description': 'Coffee Shop', 'amount': -2.50, 'balance': 5.00},
                    {'date': '2025-07-09', 'description': 'Bus Fare', 'amount': -2.25, 'balance': 7.50},
                    {'date': '2025-07-08', 'description': 'Dollar Store', 'amount': -3.75, 'balance': 9.75},
                    {'date': '2025-07-07', 'description': 'ATM Fee', 'amount': -3.00, 'balance': 13.50},
                    {'date': '2025-07-07', 'description': 'ATM Withdrawal', 'amount': -20.00, 'balance': 16.50},
                    {'date': '2025-07-05', 'description': 'Part-time Job Deposit', 'amount': 43.67, 'balance': 36.50},
                    {'date': '2025-07-04', 'description': 'Fast Food', 'amount': -8.50, 'balance': -8.50},
                    {'date': '2025-07-03', 'description': 'Overdraft Fee', 'amount': -35.00, 'balance': 0.00},
                    {'date': '2025-07-03', 'description': 'Grocery Store', 'amount': -12.25, 'balance': 35.00},
                    {'date': '2025-07-02', 'description': 'Bus Fare', 'amount': -2.25, 'balance': 47.25},
                    {'date': '2025-07-01', 'description': 'Laundromat', 'amount': -5.50, 'balance': 49.50},
                    {'date': '2025-06-28', 'description': 'Part-time Job Deposit', 'amount': 37.84, 'balance': 55.00},
                    {'date': '2025-06-27', 'description': 'Thrift Store', 'amount': -6.99, 'balance': 17.00},
                    {'date': '2025-06-26', 'description': 'Bus Fare', 'amount': -2.25, 'balance': 24.00},
                    {'date': '2025-06-25', 'description': 'Food Bank Donation', 'amount': 0.00, 'balance': 26.25},
                    {'date': '2025-06-24', 'description': 'Gas Station Snack', 'amount': -3.50, 'balance': 26.25},
                    {'date': '2025-06-22', 'description': 'Phone Card', 'amount': -9.99, 'balance': 29.75},
                    {'date': '2025-06-21', 'description': 'Part-time Job Deposit', 'amount': 32.50, 'balance': 39.75},
                    {'date': '2025-06-20', 'description': 'Library Fine', 'amount': -2.00, 'balance': 7.25},
                    {'date': '2025-06-18', 'description': 'Bus Fare', 'amount': -2.25, 'balance': 9.25}
                ]
            }
        }
    },
    
    # Variant: Retiree
    'emartinez48': {
        'password': 'Evelyn1948',
        'name': 'Evelyn Martinez',
        'email': 'evelyn.martinez@gmail.com',
        'phone': '+61 8 2222 8888',
        'routing_number': '062-692',
        'swift_code': 'NEXAAU2SXXX',
        '2fa_enabled': True,
        '2fa_method': 'email',
        '2fa_phone': '***-***-8888',
        'accounts': {
            'checking': {
                'account_number': '4029-8765-5826-9371',
                'account_type': 'Senior Checking',
                'balance': 12000.00,
                'transactions': [
                    {'date': '2025-07-10', 'description': 'Pension Deposit', 'amount': 1987.33, 'balance': 12000.00},
                    {'date': '2025-07-08', 'description': 'Pharmacy - Medicare Copay', 'amount': -14.95, 'balance': 10000.00},
                    {'date': '2025-07-05', 'description': 'Grocery Store - Senior Discount', 'amount': -87.50, 'balance': 10015.00},
                    {'date': '2025-07-03', 'description': 'Church Donation', 'amount': -87.43, 'balance': 10102.50},
                    {'date': '2025-07-01', 'description': 'HOA Fee', 'amount': -124.50, 'balance': 10189.93},
                    {'date': '2025-06-28', 'description': 'Utility Bill - Electric', 'amount': -78.25, 'balance': 10327.50},
                    {'date': '2025-06-25', 'description': 'Doctor Visit Copay', 'amount': -25.00, 'balance': 10405.75},
                    {'date': '2025-06-20', 'description': 'Social Security Deposit', 'amount': 1834.67, 'balance': 10430.75},
                    {'date': '2025-06-18', 'description': 'Book Club - Coffee', 'amount': -12.50, 'balance': 8555.75},
                    {'date': '2025-06-15', 'description': 'Medicare Supplement Premium', 'amount': -164.89, 'balance': 8568.25},
                    {'date': '2025-06-10', 'description': 'Pension Deposit', 'amount': 1987.33, 'balance': 8733.25},
                    {'date': '2025-06-08', 'description': 'Grandchildren Gift', 'amount': -197.84, 'balance': 6733.25},
                    {'date': '2025-06-05', 'description': 'Grocery Store', 'amount': -95.75, 'balance': 6931.09},
                    {'date': '2025-06-01', 'description': 'Property Tax', 'amount': -447.88, 'balance': 7029.00},
                    {'date': '2025-05-30', 'description': 'Gardening Supplies', 'amount': -35.50, 'balance': 7479.00},
                    {'date': '2025-05-25', 'description': 'Senior Center Membership', 'amount': -49.95, 'balance': 7514.50},
                    {'date': '2025-05-20', 'description': 'Social Security Deposit', 'amount': 1834.67, 'balance': 7564.50},
                    {'date': '2025-05-18', 'description': 'Pharmacy', 'amount': -22.50, 'balance': 5689.50},
                    {'date': '2025-05-15', 'description': 'Home Insurance', 'amount': -184.92, 'balance': 5712.00},
                    {'date': '2025-05-10', 'description': 'Pension Deposit', 'amount': 1987.33, 'balance': 5897.00}
                ]
            },
            'savings': {
                'account_number': '4029-8765-3658-4729',
                'account_type': 'Retirement Savings',
                'balance': 85000.00,
                'transactions': [
                    {'date': '2025-07-10', 'description': 'Interest Payment', 'amount': 50.00, 'balance': 85000.00},
                    {'date': '2025-07-01', 'description': 'Monthly Transfer from Checking', 'amount': 500.00, 'balance': 84950.00},
                    {'date': '2025-06-10', 'description': 'Interest Payment', 'amount': 48.50, 'balance': 84450.00},
                    {'date': '2025-06-01', 'description': 'Monthly Transfer from Checking', 'amount': 500.00, 'balance': 84401.50},
                    {'date': '2025-05-15', 'description': 'CD Maturation', 'amount': 5000.00, 'balance': 83901.50},
                    {'date': '2025-05-10', 'description': 'Interest Payment', 'amount': 47.50, 'balance': 78901.50},
                    {'date': '2025-05-01', 'description': 'Monthly Transfer from Checking', 'amount': 500.00, 'balance': 78854.00},
                    {'date': '2025-04-10', 'description': 'Interest Payment', 'amount': 46.75, 'balance': 78354.00},
                    {'date': '2025-04-01', 'description': 'Monthly Transfer from Checking', 'amount': 500.00, 'balance': 78307.25},
                    {'date': '2025-03-20', 'description': 'Emergency Withdrawal', 'amount': -2000.00, 'balance': 77807.25},
                    {'date': '2025-03-10', 'description': 'Interest Payment', 'amount': 47.50, 'balance': 79807.25},
                    {'date': '2025-03-01', 'description': 'Monthly Transfer from Checking', 'amount': 500.00, 'balance': 79759.75},
                    {'date': '2025-02-10', 'description': 'Interest Payment', 'amount': 47.25, 'balance': 79259.75},
                    {'date': '2025-02-01', 'description': 'Monthly Transfer from Checking', 'amount': 500.00, 'balance': 79212.50},
                    {'date': '2025-01-10', 'description': 'Interest Payment', 'amount': 46.00, 'balance': 78712.50}
                ]
            }
        }
    },
    
    # Variant: Student
    'achen22': {
        'password': 'Alexandra22!',
        'name': 'Alexandra Chen',
        'email': 'a.chen@university.edu.au',
        'phone': '+61 4 3333 1212',
        'routing_number': '062-692',
        'swift_code': 'NEXAAU2SXXX',
        '2fa_enabled': True,
        '2fa_method': 'sms',
        '2fa_phone': '***-***-1212',
        'accounts': {
            'checking': {
                'account_number': '4029-8765-2574-6938',
                'account_type': 'Student Checking',
                'balance': 120.00,
                'transactions': [
                    {'date': '2025-07-10', 'description': 'Bookstore', 'amount': -60.00, 'balance': 120.00},
                    {'date': '2025-07-08', 'description': 'Campus Coffee Shop', 'amount': -8.50, 'balance': 180.00},
                    {'date': '2025-07-07', 'description': 'Pizza Delivery', 'amount': -15.75, 'balance': 188.50},
                    {'date': '2025-07-05', 'description': 'Part-time Job Deposit', 'amount': 284.17, 'balance': 204.25},
                    {'date': '2025-07-03', 'description': 'Laundry', 'amount': -5.25, 'balance': -80.75},
                    {'date': '2025-07-02', 'description': 'ATM Fee', 'amount': -3.00, 'balance': -75.50},
                    {'date': '2025-07-02', 'description': 'ATM Withdrawal', 'amount': -20.00, 'balance': -72.50},
                    {'date': '2025-07-01', 'description': 'Dorm Room Snacks', 'amount': -12.50, 'balance': -52.50},
                    {'date': '2025-06-30', 'description': 'Student Activity Fee', 'amount': -25.00, 'balance': -40.00},
                    {'date': '2025-06-28', 'description': 'Part-time Job Deposit', 'amount': 269.83, 'balance': -15.00},
                    {'date': '2025-06-25', 'description': 'Textbook Return Refund', 'amount': 44.62, 'balance': -284.83},
                    {'date': '2025-06-22', 'description': 'Campus Meal Plan', 'amount': -349.17, 'balance': -329.45},
                    {'date': '2025-06-20', 'description': 'Study Group Pizza', 'amount': -18.50, 'balance': 20.00},
                    {'date': '2025-06-18', 'description': 'School Supplies', 'amount': -25.75, 'balance': 38.50},
                    {'date': '2025-06-15', 'description': 'Parents Transfer', 'amount': 200.00, 'balance': 64.25},
                    {'date': '2025-06-12', 'description': 'Campus Parking Fee', 'amount': -14.73, 'balance': -135.75},
                    {'date': '2025-06-10', 'description': 'Energy Drink', 'amount': -4.50, 'balance': -120.75},
                    {'date': '2025-06-08', 'description': 'Movie Night', 'amount': -11.63, 'balance': -116.25},
                    {'date': '2025-06-05', 'description': 'Part-time Job Deposit', 'amount': 254.37, 'balance': -104.62},
                    {'date': '2025-06-03', 'description': 'Overdraft Fee', 'amount': -35.00, 'balance': -359.25}
                ]
            },
            'student_loan': {
                'account_number': '4029-8765-8149-3620',
                'account_type': 'HECS-HELP Student Loan',
                'balance': -15000.00,
                'monthly_payment': 149.67,
                'interest_rate': 5.5,
                'term_remaining': '8 years',
                'next_payment_date': '2025-08-01',
                'transactions': [
                    {'date': '2025-07-01', 'description': 'Monthly Payment Received', 'amount': 149.67, 'balance': -15000.00},
                    {'date': '2025-06-01', 'description': 'Monthly Payment Received', 'amount': 149.67, 'balance': -15149.67},
                    {'date': '2025-05-01', 'description': 'Monthly Payment Received', 'amount': 149.67, 'balance': -15299.34},
                    {'date': '2025-04-01', 'description': 'Monthly Payment Received', 'amount': 149.67, 'balance': -15449.01},
                    {'date': '2025-03-01', 'description': 'Monthly Payment Received', 'amount': 149.67, 'balance': -15598.68},
                    {'date': '2025-02-01', 'description': 'Monthly Payment Received', 'amount': 149.67, 'balance': -15748.35},
                    {'date': '2025-01-15', 'description': 'Interest Capitalization', 'amount': -124.83, 'balance': -15898.02},
                    {'date': '2025-01-01', 'description': 'Monthly Payment Received', 'amount': 149.67, 'balance': -15773.19},
                    {'date': '2024-12-01', 'description': 'Monthly Payment Received', 'amount': 149.67, 'balance': -15922.86},
                    {'date': '2024-11-01', 'description': 'Monthly Payment Received', 'amount': 149.67, 'balance': -16072.53},
                    {'date': '2024-10-01', 'description': 'Monthly Payment Received', 'amount': 149.67, 'balance': -16222.20},
                    {'date': '2024-09-15', 'description': 'Semester 2 Disbursement', 'amount': -4497.83, 'balance': -16371.87},
                    {'date': '2024-09-01', 'description': 'Monthly Payment Received', 'amount': 149.67, 'balance': -11874.04},
                    {'date': '2024-08-01', 'description': 'Monthly Payment Received', 'amount': 149.67, 'balance': -12023.71},
                    {'date': '2024-07-01', 'description': 'Monthly Payment Received', 'amount': 149.67, 'balance': -12173.38}
                ]
            }
        }
    }
}
