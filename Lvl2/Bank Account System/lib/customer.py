from .bank_account import BankAccount
class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts: list[BankAccount] = []

    def open_account(self, initial_balance: float):
        if not isinstance(initial_balance, float):
            raise Exception("Please enter amount in float format")
        account_number = len(self.accounts) + 1
        new_account = BankAccount(account_number, initial_balance)
        self.accounts.append(new_account)

    def total_balance(self):
        return sum(account.balance for account in self.accounts)