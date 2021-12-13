 # Class for MapTiles
#from tage_items import Item


class GameMap():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Map: {}".format(self.name)


class MapTile():
    # Base MapTile Class - Defines the minimum items necessary to create a map tile and the minimum functions needed for them
    def __init__(self, name):
        self.name = name
        self.shortDescription = ""
        self.intro = ""
        self.tile_inspect = {}
        self.map_items = {}
        self.commonRate = 50
        self.uncommonRate = 25
        self.rareRate = 4
        self.ultraRareRate = 1
        self.noSpawnRate = 20
        self.commonSpawn = []
        self.uncommonSpawn = []
        self.rareSpawn = []
        self.ultraRareSpawn = []
        

    def intro_text(self):
        raise NotImplementedError("Create a subclass of MapTile")

    def __str__(self):
        return "Tile: {}\nDescription:{}".format(self.name, self.shortDescription)
    
    def inspect_list(self):
        if len(self.tile_inspect) > 0:
            return True
        else:
            return False
    
    def add_item(self, item, qty):
        if qty < 1:
            raise ValueError("Please use subtract_item() to remove item from MapTile")
        try:
            item.is_item() # Function should fail at this check
            if item.name.lower() in self.map_items:
                # If the item is already in the map tile
                # Increase the Value of the item's qty by qty
                self.map_items[item.name.lower()]["qty"] += qty
            else:
                self.map_items[item.name.lower()] = {
                    "item" : item,
                    "qty" : qty
                }

        except:
            raise ValueError("Item must be a tage Item() class or one of it's children")

    def remove_item(self, item):
        item = item.lower()
        try:
            if item.lower() in self.map_items:
                # If item exists in the list, check to see if there is enough qty to complete transaction
                i = self.map_items[item.lower()]["item"]
                qty = self.map_items[item.lower()]["qty"]

                del self.map_items[item]

                return [i, qty]
            raise ValueError(f"Item {item} does not exist on current map tile")
        except:
            raise ValueError("Item name does not exist in MapTile")


    def check_item(self, item):
        if item.lower() in self.map_items:
            return True
        else:
            return False


    def has_inventory(self):
        # Flag used 
        return True


    def tile_items(self):
        # Returns list of items currently in the active tile
        return self.map_items

    def set_spawn_rate(self, common, uncommon, rare, ultraRare, noSpawn):
        # Function sets a custom spawn rate for individual map tiles
        if common + uncommon + rare + ultraRare + noSpawn != 100:
            # If the numbers entered don't equall 100, scale the numbers based on the values entered
                unscaledTotal = common + uncommon + rare + ultraRare + noSpawn
                self.commonRate = (common / unscaledTotal) * 100
                self.uncommonRate = (uncommon / unscaledTotal) * 100
                self.rareRate = (rare / unscaledTotal) * 100
                self.ultraRareRate = (ultraRare / unscaledTotal) * 100
                self.noSpawnRate = (noSpawn / unscaledTotal) * 100
        else:
            self.commonRate = common
            self.uncommonRate = uncommon
            self.rareRate = rare
            self.ultraRareRate = ultraRare
            self.noSpawnRate = noSpawn

    def __add_spawn_item(self, item, spawnList):
        # PRIVATE - Adds Items to the spawnLists - Used by add_spawn_items()
        try:
            if item.is_item():
                spawnList.append(item)
        except:
            if type(item) is list:
                for i in item:
                    try:
                        if i.is_item():
                            spawnList.append(i)
                    except:
                        pass            
    
    def add_spawn_item(self, item, rateClass):
        # Adds spawn Items to the map tile
        if type(rateClass) is int:
            if rateClass == 1:
                self.__add_spawn_item(item, self.commonSpawn)

            elif rateClass == 2:
                self.__add_spawn_item(item, self.uncommonSpawn)

            elif rateClass == 3:
                self.__add_spawn_item(item, self.rareSpawn)

            elif rateClass == 4:
                self.__add_spawn_item(item, self.ultraRareSpawn)
        
            else:
                raise ValueError("Rate class must be an Integer or String 1-'common', 2-'uncommon', 3-'rare', 4-'ultrarare'")

        elif type(rateClass) is str:
            if rateClass.lower() == "common":
                self.__add_spawn_item(item, self.commonSpawn)

            elif rateClass.lower() == "uncommon":
                self.__add_spawn_item(item, self.uncommonSpawn)

            elif rateClass.lower() == "rare":
                self.__add_spawn_item(item, self.rareSpawn)

            elif rateClass.lower() == "ultrarare":
                self.__add_spawn_item(item, self.ultraRareSpawn)

            else:
                raise ValueError("Rate class must be an int or str: 1-'common', 2-'uncommon', 3-'rare', 4-'ultrarare'")

            
class StartTile(MapTile):
    
    def intro_text(self):
        return self.intro

    def short_description(self):
        return self.shortDescription


# Need to have subclasses of Map tiles
# - StartTile - will be the starting tile on a map
# - TransportTile - Will be a linking tile between 2 maps. 
# - GameTile - Will be a typical game play tiles