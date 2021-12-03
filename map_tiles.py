 # Class for MapTiles

class MapTile():
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return "Tile: {}\nDescription:{}".format(self.name, self.description)

