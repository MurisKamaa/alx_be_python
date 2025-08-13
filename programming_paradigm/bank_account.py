class BankAccount:
    def __init__(self, account_balance):
        self._account_balance = account_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._account_balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")
