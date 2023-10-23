class Item: #when creating a class the name must always by capitalized

    # The pass statement is used as a placeholder for future code.
    # When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
    # Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
    #pass 

    def calculate_total_price(self, x, y): # self is an attribute that is auto generated and python wants us to pass. Must allways pass self
                                            # python passes the object itself as a first arguement when you call those methods
                                            # when you call the method from the instance of the class python know which instance is calling the method
        return x * y

# How to create an instance of a class
item1 = Item()
# this is equivilant to creating a random str
# random_str = str("4")


# Assign attributes to the instance of a class:
# each of the attributes is assigned to one instance of the class
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

# create a second instance of a the item class.
item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3

print(type(item1)) # item: retuens a datatype of item __main__
print(type(item1.name)) #str
print(type(item1.price)) #int
print(type(item1.quantity)) #int

# Calling methods from instances of a class:

# methods are functions of a class

# example the built in class string has methods that can be called
# random_str = "aaa"
# print(random_str.upper()) # the upper method capitalizes all letters in the string


print(item1.calculate_total_price(item1.price, item1.quantity)) # when calling the method python passes item1 as self, item1.price as x, item1.quantity as y

# Calling methods from second instances of a class: 
print(item2.calculate_total_price(item2.price, item2.quantity))