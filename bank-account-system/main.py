# Import BankAccount class
from bank_account import BankAccount


# ---------- Create Savings Account ----------
savings_account = BankAccount(
    account_number="SAV1001",
    account_holder_name="Isha Rajput",
    account_type="savings",
    balance=5000
)

# Perform operations on savings account
print("\n--- Savings Account Operations ---")
print("Initial Balance:", savings_account.get_balance())
savings_account.deposit(2000)
savings_account.withdraw(4500)   # should fail (min balance)
savings_account.withdraw(1000)   # valid


# ---------- Create Current Account ----------
current_account = BankAccount(
    account_number="CUR2001",
    account_holder_name="Isha Rajput",
    account_type="current",
    balance=3000
)

# Perform operations on current account
print("\n--- Current Account Operations ---")
print("Initial Balance:", current_account.get_balance())
current_account.deposit(1000)
current_account.withdraw(3500)   # allowed for current account


# ---------- Display Account Details ----------
print("\n--- Account Details and Transaction History for saving account---")
savings_account.show_details()
savings_account.show_transaction_history()

print("\n--- Account Details and Transaction History for current account---")
current_account.show_details()
current_account.show_transaction_history()
