from src.bank.user_data import FAKE_ACCOUNTS

print("Testing min_payment field:")
wealthy = FAKE_ACCOUNTS['wealthy123']['accounts']['credit_card']
print(f"Credit card min payment: ${wealthy.get('min_payment', 'NOT FOUND')}")
print("Data loads successfully!")
