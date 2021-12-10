 
class Player:
    
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        self.money = 0
        self.posX = 0
        self.posY = 0

    def __str__(self):
        return f"Player: {self.name}"

    def adjust_inventory(self, itemKey, qty):
        ''' Adjusts players inventory, adds item if qty is positive and item does
            not currently exists in inventroy, adjusts quantity if item already exists
        '''
        # Check if item exists in inventory
        if itemKey in self.inventory.keys():
            
            # If it does, check if adjustment takes value out of bounds (<0)
            if self.inventory[itemKey] + qty >= 0:

                # If adjustment is good, make adjustment
                self.inventory[itemKey] = self.inventory[itemKey] + qty
                # If quantity is now zero remove item from inventory
                if self.inventory[itemKey] == 0:
                    self.inventory.pop(itemKey)
                return 1

            # If value takes item out of bounds (<0)
            else:
                # Make no adjustments return error
                raise ValueError(f"Not enough {itemKey} in inventory.")

        # If item does not exist in inventory Add Item to Inventory
        else:
            self.inventory[itemKey] = qty
            return 1


    def player_pos(self):

        return [self.posX, self.posY]