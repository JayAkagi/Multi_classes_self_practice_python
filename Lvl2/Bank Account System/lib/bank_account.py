class BankAccount:
    def __init__(self, account_number: int, balance: float):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount:float):
        if not isinstance(amount, float):
            raise Exception("Please enter amount in float format")
        self.balance += amount

    def withdraw(self, amount: float):
        if not isinstance(amount, float):
            raise Exception("Please enter amount in float format")
        self.balance -= amount

    def get_balance(self):
        return f"Balance: {self.balance}"