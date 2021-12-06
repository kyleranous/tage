 
class Player():
    
    def __init__(self, name):
        self.name = name
        self.inventory = {}

    def __str__(self):
        return f"Player: {self.name}"

    def adjust_inventory(self, itemKey, qty):
        
        if itemKey in self.inventory.keys():
            self.inventory[itemKey] = self.inventory[itemKey] + qty
            return 1
        
        else:
            if qty <= 0:
                return 0
            else:
                self.inventory[itemKey] = qty
                return 1