import csv


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

    # to convert this to a class method we need to use a decorator
    # decorator: decorators are a quick way to change the behavior of the function we will write, byt calling the decorator before the function

    @classmethod
    def instantiate_from_csv(cls): # we are not going to have any instances call this method from the instace
        # this method is going to be used to create instances, therefor, this method will be a class method. class methods do not use self, they use class (cls)
        # (cls) for a class method the class object itself is passed as the first argument.

        with open('items.csv', 'r') as f: # open the csv file, 'r' means read-only
            reader = csv.DictReader(f) # use reader to read content as a list of dictionaries
            items = list(reader) # convert the reader to list

        for item in items:
            # instantiate our instances
            Item(
                name=item.get('name'),
                price=float(item.get('price')), # all itmes will be passed as string from the list and need to be converted to proper datatype
                quantity=int(item.get('quantity'))

            )

    @staticmethod
    def is_integer(num): #the parameter is now a regular parameter as the static method does not send the object as a first argument.
        # We will count out the floats that are point zero
        # will return True if flot is .0
        # Foe i.e: 5.0, 10.0
        if isinstance(num, float): # if instance is float
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False



    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


phone1 = Item("JscPhonev10", 500, 5)
phone1.broken_phones = 1
phone2 = Item("jscPhonev20", 700, 5)
phone2.broken_phones = 1
