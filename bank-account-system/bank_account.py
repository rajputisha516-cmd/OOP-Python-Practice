class BankAccount:
    def __init__(self, account_number, account_holder_name, account_type, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type.lower()
        self._balance = balance
        self._transaction_history = []

        if self.account_type == "savings":
            self.minimum_balance = 1000
        elif self.account_type == "current":
            self.minimum_balance = 0
        else:
            raise ValueError("Invalid account type")

    # ---- Deposit Money ----
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            self._transaction_history.append(f"Failed deposit: ₹{amount}")
            return

        self._balance += amount
        self._transaction_history.append(f"Deposited: ₹{amount}")
        print(f"Deposited ₹{amount}. New balance is ₹{self._balance}.")

    # ---- Withdraw Money ----
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            self._transaction_history.append(f"Failed withdrawal: ₹{amount}")
            return

        if amount > self._balance:
            print("Insufficient balance.")
            self._transaction_history.append(f"Failed withdrawal: ₹{amount} (Insufficient balance)")
            return

        if self._balance - amount < self.minimum_balance:
            print("Withdrawal denied due to minimum balance rule.")
            self._transaction_history.append(
                f"Failed withdrawal: ₹{amount} (Minimum balance rule)"
            )
            return

        self._balance -= amount
        self._transaction_history.append(f"Withdrew: ₹{amount}")
        print(f"Withdrew ₹{amount}. New balance is ₹{self._balance}.")

    # ---- Get Current Balance ----
    def get_balance(self):
        return self._balance

    # ---- Show Account Details ----
    def show_details(self):
        print("\n---- Account Details ----")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Account Type: {self.account_type.capitalize()}")
        print(f"Balance: ₹{self._balance}")
        print(f"Minimum Balance Required: ₹{self.minimum_balance}")

    # ---- Show Transaction History (Loop inside class) ----
    def show_transaction_history(self):
        print("\n---- Transaction History ----")
        if not self._transaction_history:
            print("No transactions available.")
            return

        for transaction in self._transaction_history:
            print(transaction)
