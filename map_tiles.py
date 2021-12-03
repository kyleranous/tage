 # Class for MapTiles

class MapTile():
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
        
    def __str__(self):
        return "Tile: {}\nDescription:{}".format(self.name, self.description)

