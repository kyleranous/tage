
# To Do: Figure out the base item classes for use in the scripting language

class Item():
    # The Base Class for All Items
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        #self.qty = 1

    def __str__(self):
        return "{}\n-------\n{}\nValue: {}\n".format(self.name, self.description, self.value)

    def is_item(self):
        return True
    
class Gold(Item):
    # Sample Subclass of Item, Don't know if Gold will be the base curency
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A Round Coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)
