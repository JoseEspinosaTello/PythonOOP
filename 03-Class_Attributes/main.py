# Class Attributes
# An attribute that will belong to the class itself

# these attributes must be passed when an isntance of a class is created


class Item:

    # pay_rate is a class level attribute
    # when we have an instance of a class python will try to bring the attribute from the instance level first and then the class level
    pay_rate = 0.8 # The pay rate after 20% discount

  
    def __init__(self, name:str, price: float, quantity = 0): 

           
            assert price >= 0, f"Price {price} is not greater than or equal to zero!" 
            assert quantity >= 0, f"Price {price} is not greater than or equal to zero!"
            
            
            # Assign to self object
            self.name = name # now we are dynamically assiging attribute to the class
            self.price = price 
            self.quantity = quantity
            # validate the values using assert statements: used to check if there is a match between what is happening, to your expectations.
             

    def calculate_total_price(self): # this method no longer needs parameters as they have been assigned by the constructor
        return self.price * self.quantity
    
    # Method that will apply discount

    def apply_discount(self):
         self.price = self.price * self.pay_rate #chagne pay_rate from class level to instance level Item.pay_rate > self.pay_rate


item1 = Item("Phone", 100, 1)
item1.apply_discount()
print(item1.price)

item2 = Item( "Laptop", 1000, 3) 
# apply a specific discount to an instance of a class

item2.pay_rate = 0.7 # for item2 it will find the pay_rate attribute in the instance level

item2.apply_discount()
print(item2.price) # first try it still used the pay_rate of the class level, this is because in the method we are using the class level attribute.


# list the attributes 
# print(Item.__dict__) # list the attributes for class level
# print("Instance")
# print(item1.__dict__) # list the attributes for instance level
