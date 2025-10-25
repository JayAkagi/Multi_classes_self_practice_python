from lib.item import Item
from lib.cart import Cart

orange = Item("Orange", 2.00)
apple = Item("Apple", 2.50)
milk = Item("Milk", 3.55)
chocolate = Item("Chocolate", 3.70)
juice = Item("Juice", 3.91)

cart1 = Cart()
cart2 = Cart()

cart1.add_item(orange)
cart1.add_item(apple)
cart1.add_item(juice)
cart1_total = cart1.total()

print("==== CART 1 ====")
cart1.print_items()
print(f"TOTAL: £{cart1_total}")