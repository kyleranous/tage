
# To Do: Figure out the base item classes for use in the scripting language

class Item():
    # The Base Class for All Items
    def __init__(self, name, description, value):
        
        if type(name) != str:
            raise TypeError("Name must be a string")
        self.name = name

        if type(description) != str:
            raise TypeError("Description must be a string")
        self.description = description

        if type(value) != int:
            raise TypeError("Value must be an integer")
        self.value = value


    def __str__(self):
        return "{}\n-------\n{}\nValue: {}\n".format(self.name, self.description, self.value)

    def is_item(self):
        return True
    