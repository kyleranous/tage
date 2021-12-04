 # Class for MapTiles

class MapTile():
    
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass of MapTile")

    def __str__(self):
        return "Tile: {}\nDescription:{}".format(self.name, self.shortDescription)


# Need to have subclasses of Map tiles
# - StartTile - will be the starting tile on a map
# - TransportTile - Will be a linking tile between 2 maps. 
# - GameTile - Will be a typical game play tiles