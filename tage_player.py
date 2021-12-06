 
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
            # If it does, check if adjustment takes value out of bounds (<0)
                # If adjustment is good, make adjustment
                # If quantity is now zero remove item from inventory
                # Return success
            # If value takes item out of bounds (<0)
                # Make no adjustments return error
        # If item does not exist in inventory Add Item to Inventory
            # Return Success


