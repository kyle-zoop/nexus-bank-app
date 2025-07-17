from src.bank.user_data import FAKE_ACCOUNTS

print("Sample realistic amounts after updates:")
print(f"Student part-time job: ${FAKE_ACCOUNTS['student1']['accounts']['checking']['transactions'][3]['amount']}")
print(f"Student loan payment: ${FAKE_ACCOUNTS['student1']['accounts']['student_loan']['monthly_payment']}")
print(f"Middle class rent: ${FAKE_ACCOUNTS['demo123']['accounts']['checking']['transactions'][6]['amount']}")
print(f"Middle class savings transfer: ${FAKE_ACCOUNTS['demo123']['accounts']['savings']['transactions'][1]['amount']}")
print(f"Retiree church donation: ${FAKE_ACCOUNTS['retiree']['accounts']['checking']['transactions'][2]['amount']}")
print(f"Wealthy charity donation: ${FAKE_ACCOUNTS['wealthy123']['accounts']['checking']['transactions'][13]['amount']}")
