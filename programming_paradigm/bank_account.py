class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}.")
