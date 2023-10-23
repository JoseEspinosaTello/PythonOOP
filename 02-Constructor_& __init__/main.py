# __nit__ can also be called constructor
# allow us to set instance attributes
# these attributes must be passed when an isntance of a class is created


class Item:

    # __init__ is a magic method
    def __init__(self, name:str, price: float, quantity = 0): # we can set default values, and assignt 
         #print("I am created") # example to show that the constructor is called when instance is created.
            #print(f"An instance created: {name}")

            # Run validations to recieve arguments.
            # validate the values using assert statements: used to check if there is a match between what is happening, to your expectations.

            assert price >= 0, f"Price {price} is not greater than or equal to zero!" # if values does not meet statement it will throw assertion error
            assert quantity >= 0, f"Price {price} is not greater than or equal to zero!" # ex.. -1 will throw assertion error
            
            
            # Assign to self object
            self.name = name # now we are dynamically assiging attribute to the class
            self.price = price 
            self.quantity = quantity
            # validate the values using assert statements: used to check if there is a match between what is happening, to your expectations.
            

    def calculate_total_price(self): # this method no longer needs parameters as they have been assigned by the constructor
        return self.price * self.quantity


item1 = Item("Phone", 100, 1) # will run the contructor and return "I am created"
# item1.name = "Phone" # now that class has dynamic attributes from contructor we no longer need to et attributes outside the class
# item1.price = 100
# item1.quantity = 5


item2 = Item( "Laptop", 1000, 3) # will run constructor and return "I am created"
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3

# We can still assign attributes to specific instances individually
# ex.. if you want to determine if laptop has a numpad or not but this is not an attribute you want to assign to a phone
# Just because you assigned attributes using the constructor doesnt mean you can't assign attributes to an isntance of the class,
item2.has_numpad = False



print(item1.calculate_total_price())
print(item2.calculate_total_price())
# print(item1.name)
# print(item1.price)
# print(item1.quantity)
# print(item2.name)
# print(item2.price)
# print(item2.quantity)