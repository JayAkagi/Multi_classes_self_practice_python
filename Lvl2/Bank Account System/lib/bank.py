from .customer import Customer
class Bank:
    def __init__(self):
        self.customers: list[Customer] = []

    def add_customer(self, customer: Customer):
        if not isinstance(customer, Customer):
            raise Exception("Only Instance of customer can be added.")
        self.customers.append(customer)

    def find_customer(self, name:str):
        for customer in self.customers:
            if name == customer.name:
                return customer
        return None