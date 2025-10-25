from .item import Item
class Cart:
    def __init__(self):
        self.items: list[Item] = []

    def add_item(self, item: Item):
        if not isinstance(item, Item):
            raise Exception("only instance of Item can be added.")
        self.items.append(item)

    def total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
    
    def print_items(self):
        print("Your Cart")
        for item in self.items:
            print(item)