 # Class for MapTiles

class MapTile():
    
    def __init__(self, name, shortDescription):
        self.name = name
        self.shortDescription = shortDescription
        self.longDescription = shortDescription
        self.items = []
        self.newTile = True

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def __str__(self):
        return "Tile: {}\nDescription:{}".format(self.name, self.shortDescription)
