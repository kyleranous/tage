 
class Player():
    
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
        if itemKey in self.inventory.keys():
            # Check if inventory adjustment will lead to a negative number
            self.inventory[itemKey] = self.inventory[itemKey] + qty
            
            if self.inventory[itemKey] <= 0: # Remove item if quantity is less then or equal to 0
                del(self.inventory[itemKey])
            
            return 1
        
        else:
            if qty <= 0:
                return 0
            else:
                self.inventory[itemKey] = qty
                return 1

