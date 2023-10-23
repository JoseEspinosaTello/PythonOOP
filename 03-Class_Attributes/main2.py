# Assigning each instance of the class to a list
# dont have a resource were we can access all items in the class
# need a list with all items instances that have been created up to this point.
# we will create a class attribute named all and will add our instances to this list.

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = [] # empty list where we will add our intem isntances

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        # this will add the class isntance to the list
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all) # this will print a list with 5 instances, each instance will look like this
# <__main__.Item object at 0x000001BA57292208>

# the __rep__ function allows us to change what is displayed

# loop that better displays this
for instance in Item.all:
    print(instance.name)