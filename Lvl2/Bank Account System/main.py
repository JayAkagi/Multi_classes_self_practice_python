from lib.bank_account import BankAccount
from lib.bank import Bank
from lib.customer import Customer

greedy_bank = Bank()

customer1 = Customer("John")
customer2 = Customer("Doe")

greedy_bank.add_customer(customer1)
greedy_bank.add_customer(customer2)

customer1.open_account(1000.0)
customer2.open_account(500.0)

print(f"Customer: {customer1.name}")
for account in customer1.accounts:
    print(f"Account {account.account_number} - {account.get_balance()}")

customer1.accounts[0].deposit(200.0)
print(f"John new balance after deposit- {customer1.accounts[0].get_balance()}")

customer1.accounts[0].withdraw(300.10)
print(f"John new balance after withdraw- {customer1.accounts[0].get_balance()}")

found_customer = greedy_bank.find_customer("John")
if found_customer:
    print(f"{found_customer.name} is found")
else:
    print(f"{found_customer} not found.")