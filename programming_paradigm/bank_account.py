class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        if self.account_balance == int(self.account_balance):
            amount = int(self.account_balance)
        else:
            amount = self.account_balance
        print(f"Current Balance: ${amount}")
