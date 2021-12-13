# Class for MapTiles
import random


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
        self.tileInspect = {}
        # Inventory Management
        self.map_items = {}
        # Spawn Management
        self.commonRate = 0.503
        self.uncommonRate = .25
        self.rareRate = .04
        self.ultraRareRate = .007 
        self.noSpawnRate = .2 
        self.commonSpawn = []
        self.uncommonSpawn = [] 
        self.rareSpawn = []
        self.ultraRareSpawn = []
        self.spawnRates = []
        self.spawnRates.append(int(self.noSpawnRate * 1000))
        self.spawnRates.append(self.spawnRates[0] + int(self.commonRate*1000))
        self.spawnRates.append(self.spawnRates[1] + int(self.uncommonRate*1000))
        self.spawnRates.append(self.spawnRates[2] + int(self.rareRate*1000))
        self.spawnRates.append(self.spawnRates[3] + int(self.ultraRareRate*1000))
        

    def intro_text(self):
        raise NotImplementedError("Create a subclass of MapTile")

    def __str__(self):
        return "Tile: {}\nDescription:{}".format(self.name, self.shortDescription)
    
    def inspect_list(self):
        if self.tileInspect:
            return True
        else:
            return False
    
    def add_item(self, item, qty):
        # Adds Item to the Maps Inventory
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
        if common + uncommon + rare + ultraRare + noSpawn != 1:
            # If the numbers entered don't equall 100, scale the numbers based on the values entered
                unscaledTotal = common + uncommon + rare + ultraRare + noSpawn
                self.commonRate = (common / unscaledTotal)
                self.uncommonRate = (uncommon / unscaledTotal)
                self.rareRate = (rare / unscaledTotal)
                self.ultraRareRate = (ultraRare / unscaledTotal)
                self.noSpawnRate = (noSpawn / unscaledTotal)
        else:
            self.commonRate = common
            self.uncommonRate = uncommon
            self.rareRate = rare
            self.ultraRareRate = ultraRare
            self.noSpawnRate = noSpawn

        self.spawnRates.clear()
        self.spawnRates.append(int(self.noSpawnRate * 1000))
        self.spawnRates.append(self.spawnRates[0] + int(self.commonRate*1000))
        self.spawnRates.append(self.spawnRates[1] + int(self.uncommonRate*1000))
        self.spawnRates.append(self.spawnRates[2] + int(self.rareRate*1000))
        self.spawnRates.append(self.spawnRates[3] + int(self.ultraRareRate*1000))

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

    def __spawn_item(self, itemList):
        pass
        random.shuffle(itemList)
        self.add_item(itemList[0], 1)

    
    def spawn_item(self):
        spawnNumber = int(random.random() * 1000)

        if spawnNumber in range(0, self.spawnRates[0]):
            # Do not spawn an item into the tile
            pass

        elif spawnNumber in range(self.spawnRates[0], self.spawnRates[1]):
        
            if self.commonSpawn: # If commonSpawn list is not empty, pass it to __spawn_item()
                self.__spawn_item(self.commonSpawn)

        elif spawnNumber in range(self.spawnRates[1], self.spawnRates[2]):

            if self.uncommonSpawn: # If uncommonSpawn list is not empty, pass it to __spawn_item()
                self.__spawn_item(self.uncommonSpawn)

        elif spawnNumber in range(self.spawnRates[2], self.spawnRates[3]):
            
            if self.rareSpawn: # If rareSpawn list is not empty, pass it to __spawn_item()
                self.__spawn_item(self.rareSpawn)

        elif spawnNumber in range(self.spawnRates[3], self.spawnRates[4]):
            
            if self.ultraRareSpawn: # If ultraRareSpawn list is not empty, pass it to __spawn_item()
                self.__spawn_item(self.ultraRareSpawn)

class StartTile(MapTile):
    
    def intro_text(self):
        return self.intro

    def short_description(self):
        return self.shortDescription


# Need to have subclasses of Map tiles
# - StartTile - will be the starting tile on a map
# - TransportTile - Will be a linking tile between 2 maps. 
# - GameTile - Will be a typical game play tiles