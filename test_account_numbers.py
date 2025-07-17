from src.bank.user_data import FAKE_ACCOUNTS

print("Updated Account Numbers:")
print("=" * 40)

for username, user_data in FAKE_ACCOUNTS.items():
    print(f"\n{user_data['name']} ({username}):")
    for account_type, account in user_data['accounts'].items():
        print(f"  {account_type}: {account['account_number']}")
