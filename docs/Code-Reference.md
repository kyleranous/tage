## module::tagemap
---
### Class::GameMap()
```python
from modules.tagemap import GameMap
```

---
### Class::MapTile()
```python
from modules.tagemap import MapTile
```
MapTile is the base class for game play tiles that create the playable map. 
```python
m = MapTile("Tile Name")
```
#### Class Variables

##### name
*string*
Name of the map tile, set when MapTile object is initialized. Renders at the top of the screen when tile is active.

##### shortDescription
*string*
Short text description of the tile. Used to pass information to the player
**Default Value: empty**

##### intro
*string*
Introduction text displayed to the player the first time they visit a tile
**Default Value: empty**

##### tileInspect
*dict*
Dictionary that holds custom inspectable objects for the map tile. Not fully implemented yet.
**Default Value: {}**

##### map_items
*dict*
Dictionary that holds the map inventory. Inventory is defined as items the player can interact with. Do not updated manually. Use [add_item()](#add_item) or [remove_item()](#remove_item) functions to manipulate the dictionary.

```python
>>> from modules.tagemap import MapTile
>>> from modules.tageitem import Item
>>> 
>>> m = MapTile("Test Tile")
>>> i = Item("Test Item", "This is a test item", 100)
>>> m.add_item(i, 2)
>>> m.map_items

{'test item': {'item': <modules.tageitem.Item object at 0x000001F976A8D340>, 'qty': 2}}
```
**Default Value: {}**

##### commonRate
*float*
Rate that common items are spawned in the map tile. Do not update manually. Use [set_spawn_rate()](#set_spawn_rate) to set custom spawn rates.
**Default Value: 0.503**

##### uncommonRate
*float*
Rate that uncommon items are spawned in the map tile. Do not update manually. Use [set_spawn_rate()](#set_spawn_rate) to set custom spawn rates.
**Default Value: 0.25**

##### rareRate
*float*
Rate that Rare items are spawned in the map tile. Do not update manually. Use [set_spawn_rate()](#set_spawn_rate) to set custom spawn rates.
**Default Value: .04**

##### ultraRareRate
*float*
Rate that Ultra-Rare items are spawned in the map tile. Do not update manually. Use [set_spawn_rate()](#set_spawn_rate) to set custom spawn rates.
**Default Value: .007**

##### noSpawnRate
*float*
Rate that No Item will spawn in the map tile. Do not update manually. Use [set_spawn_rate()](#set_spawn_rate) to set custom spawn rates.
**Default Value: .2*

##### commonSpawn
*list*
List of items that will spawn at the common rate. Items are chosen from the list at random. Do not update manually. Use [add_spawn_item()](#add_spawn_item) to add items to spawn list.
**Default Value: []**

##### uncommonSpawn
*list*
List of items that will spawn at the uncommon rate. Items are chosen from the list at random. Do not update manually. Use [add_spawn_item()](#add_spawn_item) to add items to spawn list.
**Default Value: []**

##### rareSpawn
*list*
List of items that will spawn at the rare rate. Items are chosen from the list at random. Do not update manually. Use [add_spawn_item()](#add_spawn_item) to add items to spawn list.
**Default Value: []**

##### ultraRareSpawn
*list*
List of items that will spawn at the ultra-rare rate. Items are chosen from the list at random. Do not update manually. Use [add_spawn_item()](#add_spawn_item) to add items to spawn list.
**Default Value: []**

##### spawnRates
*list*
List of spawn rates adjusted to be used with spawn function. Do not manipulate. List is populated automatically when spawn rates are changed with [add_spawn_item()](#add_spawn_item).
**Default Value: [200, 703, 953, 993, 1000]**

#### Class Functions:

##### intro_text()

##### __str__()
Returns a string
```python
>>> from modules.tagemap import MapTile
>>> 
>>> m = MapTile("Test Tile")
>>> m.shortDescription = "This is a test tile."
>>> 
>>> print(m)

Tile: Test Tile
Description:This is a test tile.
```
##### inspect_list()
*bool*
Returns True if inspect_list is not empty, false if it is empty.
##### add_item(item, qty)
Adds an item to the Map Tiles Inventory. Qty must be greater then or equal to 1. 

```python
>>> from modules.tagemap import MapTile
>>> from modules.tageitem import Item
>>> 
>>> m = MapTile("Test Tile")
>>> i = Item("Test Item", "This is a test item.", 100)
>>> 
>>> m.add_item(i, 3)  # Add (3) item i to map inventory  
>>> 
>>> m.map_items
{'test item': {'item': <modules.tageitem.Item object at 0x0000023A4A68D340>, 'qty': 3}}
```

##### remove_item(itemName)
Removes item from the map tile inventory by name. Expects a string.

```python
...
>>> m.remove_item(i.name)
>>>
>>> m.map_items
{}
```
##### check_item(itemName)
*bool*
Checks if an item exists in the map inventory. Expects a string. Returns True if item name exists as a key in map_items, False if the item name is not a key in map_items.

##### has_inventory()
Returns True. Function is used as a check in the [transfer_item()](#transfer_item) function.

#### set_spawn_rate(common, uncommon, rare, ultraRare, noSpawn)

#### __add_spawn_item()
*PRIVATE FUNCTION*

See [add_spawn_item()](#add_spawn_item)

#### add_spawn_item()

#### __spawn_item()
*PRIVATE FUNCTION*

See [spawn_item()](#spawn_item)

#### spawn_item()

---
## Class::StartTile()
*Module: tage_map*

*Extends [MapTile()](#maptile)*

**Class Functions**:

## Class::TitleScreen()

### Class Variables
* title
* titleFont
* width
* color
* bannerText
* bannerColor
* caption
* menu

### Class Functions:
**add_title_line()**

**add_banner_line()**

**add_menu_item()**

**render_title()**

**render_menu()**

**render_title_screen()**

#### ex:
```python
    from tage_title_screen import *

    # Add Title Screen Text
    testScreen = TitleScreen(title="G A M E")
    testScreen.add_title_line("T I T L E")
    # Set Title Screen Text Color
    testScreen.color = "green"
    # Add Caption
    testScreen.caption = "Version 0.1alpha(DEMO)"
    # Set Title Screen Width
    testScreen.width = 100
    # Add Banner Text
    testScreen.add_banner_line("This is a banner!")
    testScreen.add_banner_line("Where you can put your game tagline.")
    # Set Banner Color
    testScreen.bannerColor = "blue"
    # Add Title Screen Menu
    testScreen.add_menu_item(["Continue", "New Game", "Settings", "Quit", "Menu Item", "Another Menu Item"])
    # Render Title Screen
    testScreen.render_title_screen()
```
![title_screen](images/title_screen.png)
# Modules

## tageutils
### clearScreen()
OS independed method of clearing the console

### transfer_item()
Transfers an inventory item between two(2) objects with an inventory

**ex:**
```python
from tageutils import *
from tage_player import Player
from tage_items import Item
from tage_map import MapTile

# Create Player, Item, and MapTile Objects
p = Player("Test Player")
i = Item("Test Item", "This is a test item.", 100)
m = MapTile("Test Tile")

# Add one(1) "Test Item" to MapTile Inventory
m.add_item(i, 1)

# Check m and p for item in inventory
m.check_item("test item")
'True'

p.check_item("test item")
'False'

# Transfer item from the MapTile to the Player
transfer_item(i, m, p)

# Check m and p for item in inventory
m.check_item("test item")
'False'

p.check_item("test item")
'True'
```