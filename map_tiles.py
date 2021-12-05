 # Class for MapTiles

class Map():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Map: {}".format(self.name)

class MapTile():
    
    def __init__(self, name):
        self.name = name
        self.shortDescription = ""
        self.intro = ""

    def intro_text(self):
        raise NotImplementedError("Create a subclass of MapTile")

    def __str__(self):
        return "Tile: {}\nDescription:{}".format(self.name, self.shortDescription)

class StartTile(MapTile):

    def intro_text(self):
        return self.intro

    def short_description(self):
        return self.shortDescription

# Need to have subclasses of Map tiles
# - StartTile - will be the starting tile on a map
# - TransportTile - Will be a linking tile between 2 maps. 
# - GameTile - Will be a typical game play tiles