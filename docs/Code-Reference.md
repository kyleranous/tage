# TAGE Code Reference

---

# module::tageitem
---
## Class::Item(name, description, value)
```python
from modules.tageitem import Item
```
### Class Variables

#### name
*string*

Name of item. Must be a string. Does not need to be unique, but not having unique item names may confuse players

#### description
*string*

Description of item. Text that is displayed when player inspects an item. Must be a string.

#### value
*int*

Value of item, used for purchasing items. There is not a current mechanic in the engine that uses this.

### Class Functions

#### \_\_str\_\_()

Returns a formatted string with the item name, description, and value

```python
>>> from modules.tageitem import Item
>>>
>>> i = Item("Test Item", "This is a test item.", 100)
>>> print(i)
Test Item
-------
This is a test item.
Value: 100
```

#### is_item()

Returns true. Function used to verify if objects passed to inventories are Item class.

---
# module::tagemap
---
## Class::GameMap()
```python
from modules.tagemap import GameMap
```

---
## Class::MapTile()
```python
from modules.tagemap import MapTile
```
MapTile is the base class for game play tiles that create the playable map. 
```python
m = MapTile("Tile Name")
```
### Class Variables

#### name
*string*

Name of the map tile, set when MapTile object is initialized. Renders at the top of the screen when tile is active.

#### shortDescription
*string*

Short text description of the tile. Used to pass information to the player

**Default Value: empty**

#### intro
*string*

Introduction text displayed to the player the first time they visit a tile

**Default Value: empty**

#### tileInspect
*dict*

Dictionary that holds custom inspectable objects for the map tile. Not fully implemented yet.

**Default Value: {}**

#### mapItems
*dict*

Dictionary that holds the map inventory. Inventory is defined as items the player can interact with. Do not updated manually. Use [add_item()](#add_item) or [remove_item()](#remove_item) functions to manipulate the dictionary.

```python
>>> from modules.tagemap import MapTile
>>> from modules.tageitem import Item
>>> 
>>> m = MapTile("Test Tile")
>>> i = Item("Test Item", "This is a test item", 100)
>>> m.add_item(i, 2)
>>> m.mapItems

{'test item': {'item': <modules.tageitem.Item object at 0x000001F976A8D340>, 'qty': 2}}
```
**Default Value: {}**

#### commonRate
*float*

Rate that common items are spawned in the map tile. Do not update manually. Use [set_spawn_rate()](#set_spawn_rate) to set custom spawn rates.

**Default Value: 0.503**

#### uncommonRate
*float*

Rate that uncommon items are spawned in the map tile. Do not update manually. Use [set_spawn_rate()](#set_spawn_rate) to set custom spawn rates.

**Default Value: 0.25**

#### rareRate
*float*

Rate that Rare items are spawned in the map tile. Do not update manually. Use [set_spawn_rate()](#set_spawn_rate) to set custom spawn rates.

**Default Value: .04**

#### ultraRareRate
*float*

Rate that Ultra-Rare items are spawned in the map tile. Do not update manually. Use [set_spawn_rate()](#set_spawn_rate) to set custom spawn rates.

**Default Value: .007**

#### noSpawnRate
*float*

Rate that No Item will spawn in the map tile. Do not update manually. Use [set_spawn_rate()](#set_spawn_rate) to set custom spawn rates.

**Default Value: .2**

#### commonSpawn
*list*

List of items that will spawn at the common rate. Items are chosen from the list at random. Do not update manually. Use [add_spawn_item()](#add_spawn_item) to add items to spawn list.

**Default Value: []**

#### uncommonSpawn
*list*

List of items that will spawn at the uncommon rate. Items are chosen from the list at random. Do not update manually. Use [add_spawn_item()](#add_spawn_item) to add items to spawn list.

**Default Value: []**

#### rareSpawn
*list*

List of items that will spawn at the rare rate. Items are chosen from the list at random. Do not update manually. Use [add_spawn_item()](#add_spawn_item) to add items to spawn list.

**Default Value: []**

#### ultraRareSpawn
*list*

List of items that will spawn at the ultra-rare rate. Items are chosen from the list at random. Do not update manually. Use [add_spawn_item()](#add_spawn_item) to add items to spawn list.

**Default Value: []**

#### spawnRates
*list*

List of spawn rates adjusted to be used with spawn function. Do not manipulate. List is populated automatically when spawn rates are changed with [add_spawn_item()](#add_spawn_item).

**Default Value: [200, 703, 953, 993, 1000]**

### Class Functions:

#### intro_text()

#### \_\_str\_\_()
Returns the class string.
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
#### inspect_list()
*bool*

Returns True if inspect_list is not empty, false if it is empty.
#### add_item(item, qty)
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
>>> m.mapItems
{'test item': {'item': <modules.tageitem.Item object at 0x0000023A4A68D340>, 'qty': 3}}
```

#### remove_item(itemName)
Removes item from the map tile inventory by name. Expects a string. Function will check if item exists and will raise a RuntimeError if item is not found in Tile's inventory.

```python
...
>>> m.remove_item(i.name)
>>>
>>> m.mapItems
{}
```
#### check_item(itemName)
*bool*

Checks if an item exists in the map inventory. Expects a string. Returns True if item name exists as a key in mapItems, False if the item name is not a key in mapItems.

#### has_inventory()
Returns True. Function is used as a check in the [transfer_item()](#transfer_item) function.

#### set_spawn_rate(common, uncommon, rare, ultraRare, noSpawn)
Set custom spawn rates. Use zero to turn a spawn off. IE, setting noSpawn to 0 would mean the random spawn generator would always spawn an item. Setting Ultra-Rare to zero would never spawn an ultra-rare item. Values must sum to 1.0. Function will scale the values automatically if they do not sum to 1.0.

```python
>>> from modules.tagemap import MapTile
>>> 
>>> m = MapTile("Test Tile")
>>>
>>> # Set Common Spawn to 40%, Uncommon to 30%
>>> # Rare to 20%, Ultra-Rare to 5%, and 
>>> # No Spawn to 5%
>>> m.set_spawn_rate(0.4, 0.3, 0.2, 0.05, 0.05)
>>> m.spawnRates
[50, 450, 750, 950, 1000]
>>>
>>> # Set Common Spawn to 40%, Uncommon to 30%
>>> # Rare to 20%, Ultra-Rare to 10% and
>>> # No Spawn to 0%
>>> m.set_spawn_rate(0.4, 0.3, 0.2, 0.1, 0)
>>> m.spawnRates
[0, 400, 700, 900, 1000]
>>>
>>> # Set Common Spawn to 40%, Uncommon to 30%
>>> # Rare to 20%, Ultra-Rare to 0% and
>>> # No Spawn to 0%
>>> m.set_spawn_rate(0.4, 0.3, 0.2, 0, 0.1)
>>> m.spawnRates
[100, 500, 800, 1000, 1000]
```
#### __add_spawn_item()
*PRIVATE FUNCTION*

See [add_spawn_item()](#add_spawn_item)

#### add_spawn_item(item, rateClass)
Adds an item to one of the spawn class lists. *item* can be a single Item object or a list of Item objects. rateClass can be an integer or a string:
<table style="margin-left: auto; margin-right: auto;">
    <tr>
        <th>int</th><th>str</th>
    </tr>
    <tr>
        <td>1</td><td>common</td>
    </tr>
    <tr>
        <td>2</td><td>uncommon</td>
    </tr>
    <tr>
        <td>3</td><td>rare</td>
    </tr>
    <tr>
        <td>4</td><td>ultrarare</td>
    </tr>
</table>
<br>
```python
>>> from modules.tagemap import MapTile
>>> from modules.tageitem import Item
>>> 
>>> m = MapTile("Test Tile")
>>> # Create Common Item
>>> c = Item("Common Item", "This is a common item", 100)
>>> # Add Common Item to Tile
>>> m.add_spawn_item(c, "common")
>>> m.commonSpawn
[<modules.tageitem.Item object at 0x000001AD7ED1D340>]
>>>
>>> # Create Several Uncommon Items
>>> u = Item("Uncommon Item", "This is an Uncommon Item", 200)
>>> u2 = Item("Uncommon Item 2", "This is another Uncommon Item", 200)
>>> u3 = Item("Uncommon Item 3", "Yet another Uncommon Item", 200)
>>> # Create list of uncommon items
>>> itemList = [u, u2, u3]
>>> # Add Uncommon Item List to Tile
>>> m.add_spawn_item(itemList, 2)
>>> m.uncommonSpawn
[<modules.tageitem.Item object at 0x000001AD7ED30520>, <modules.tageitem.Item object at 0x000001AD7ED30490>, <modules.tageitem.Item object at 0x000001AD7ED8FA00>]
>>>
```
#### __spawn_item()
*PRIVATE FUNCTION*

See [spawn_item()](#spawn_item)

#### spawn_item()
Will spawn a single item. A random number generator will select the spawn range, then an item will be chosen randomly from the spawn list and be added to the tile's inventory.

```python
>>> from modules.tagemap import MapTile
>>> from modules.tageitem import Item
>>> 
>>> m = MapTile("Test Tile")
>>> # Create Common, Uncommon, Rare, and Ultra-Rare Items
>>> c = Item("Common Item", "This is a common item", 100)
>>> u = Item("Uncommon Item", "This is an uncommon item", 200)
>>> r = Item("Rare Item", "This is a rare item", 300)
>>> ur = Item("Ultra-Rare Item", "This is an Ultra-Rare item", 400)
>>> 
>>> # Set Spawn Rates to 25%
>>> m.set_spawn_rate(0.25, 0.25, 0.25, 0.25, 0)
>>> 
>>> # Add Spawn Items to Spawn Lists
>>> m.add_spawn_item(c, 1)
>>> m.add_spawn_item(u, 2)
>>> m.add_spawn_item(r, 3)
>>> m.add_spawn_item(ur, 4)
>>> 
>>> #Spawn an item to MapTile
>>> m.spawn_item()
>>> 
>>> m.mapItems
{'common item': {'item': <modules.tageitem.Item object at 0x0000019EDFDED340>, 'qty': 1}}
```
---
## Class::StartTile()
*Module: tagemap*

*Extends [MapTile()](#maptile)*

**Class Functions**:

# Module::tageplayer
---

## Class::Player(name)
```python
from modules.modulename import Player
```

### Class Variables

#### name
*str*

Name variable stores the player's name.

#### inventory
*dict*

inventory dictionary stores the players inventory (Item's the player can activly engage with.)

#### money
*int*

variables stores the money the player has available to them. No mechanic currently exists for this variable and is in place for future use.

#### posX
*int*

Players X position on the map.

#### posY
*int*

Player's Y position on the map.

### Class Functions
---

#### \_\_str\_\_()

Returns a formatted string with the player's name

```python
>>> from modules.tageplayer import Player
>>>
>>> p = Player("Test Player")
>>>
>>> print(p)
Player: Test Player
```

#### add_item(item, qty)
Adjusts players inventory, adds item if qty is positive and item does not currently exists in inventory, adjusts quantity if item already exists. qty must be greater then or equal to 1

```python
>>> from modules.tageplayer import Player
>>> from modules.tageitem import Item
>>>
>>> p = Player("Test Player")
>>> i = Item("Test Item", "This is a test item", 100)
>>>
>>> p.add_item(i, 1)
{'test item': {'item': <modules.tageitem.Item object at 0x0000014D7255D340>, 'qty': 1}}
```

#### remove_item(itemName)
Removes an item from the player's inventory if the itme exists. Returns a runtime error if the item does not exist. itemName is a string object.

```python
...
>>> p.remove_item(i.name)
>>>
>>> p.inventory
{}
```

#### check_item(itemName)
*bool*
Returns true if the player has an item in their inventory with the name 'itemName', returns false if the item is not present in the player's inventory

```python
>>> from modules.tageplayer import Player
>>> from modules.tageitem import Item
>>>
>>> p = Player("Test Player")
>>> i = Item("Test Item", "This is a test item", 100)
>>>
>>> p.add_item(i, 1)
>>>
>>> p.check_item(i.name)
True
>>> p.remove_item(i.name)
>>> p.check_item(i.name)
False
```

#### has_inventory()
Returns True. Function is used as a flag for the [transfer_item()](#functiontransfer_itemitem-fromobj-toobj) function.

#### player_pos()
Returns a list with the players current position. `[posX, posY]`

#### update_pos(dx, dy)
Incrimentally updates the players position. dx and dy are integers and denote the change in X or Y position. if the player's current position is `[1, 1]` and `update_pos(1, 0)` is called, the player's updated position would be `[2, 1]`. If we then call `update_pos(0, -1)`, the player's updated position would now be `[2, 0]`. 

```python
>>> from modules.tageplayer import Player
>>>
>>> p = Player("Test Player")
>>> p.player_pos()
[0, 0]
>>> p.update_pos(1, 0)
>>> p.player_pos()
[1, 0]
>>> p.update_pos(1, 1)
>>> p.player_pos()
[2, 1]
>>> p.update_pos(0, -1)
>>> p.player_pos()
[2, 0]
```

#### set_pos(posX, posY)

Sets the player's position on the map. posX and posY set the absolute coordinates of the player's position. posX and posY must be integers

```python
>>> from modules.tageplayer import Player
>>>
>>> p = Player("Test Player")
>>> p.player_pos()
[0, 0]
>>> p.set_pos(2, 3)
>>> p.player_pos()
[2, 3]
```
# Module::tagesplash
---
## Class::TitleScreen()
```python
from modules.tagesplash import TitleScreen
```
### Class Variables

#### title
*list*

Game title, will be rendered in ascii art format. Each list item will be one rendered line.

**Default Value: []**

#### titleFont
*str*

Font that the title is rendered in.

Good font options:
* basic
* big
* colossal
* cyberlarge
* cybermedium
* doom
* EPIC
* fender
* ogre
* pebbles
* poison
* puffy
* roman
* rounded
* shadow
* slant
* standard
* starwars
* univers

For a full list of available fonts see the [figlet](http://www.figlet.org/fontdb.cgi) website

**Default Value: "big"**

#### width
*int*

Width of the title screen in columns (1 character is 1 column). Increase the column count to prevent title from wrapping.

**Default Value: 100**

#### color
*str*

Color of the game title. 
Options:
* "blue"
* "green"
* "red"
* "yellow"
* "black"
* "cyan"
* "magenta"

**Default Value:** `None`

#### bannerText
*list*

List of strings rendered in the banner. Each list item will be a line in the banner.

**Default Value: []**


#### caption
*str*
Caption renders a single line of text under the game title.

**Default Value:** `None`

#### menu
*list*

List of String objects which will be rendered as Menu Items. 

**Default Value: []**

#### menuCol
*int*

Number of columns the menu should be rendered in.

**Default Value: 3**

### Class Functions:

#### add_title_line()
Adds a string item to the title list. Each list entry will be (1) Line of text. Reccomendation is to keep title text to no more then 2 lines.

```python
>>>from modules.tagesplash import TitleScreen
>>>
>>> t = TitleScreen()
>>> t.add_title_line('G A M E')
>>> t.add_title_line('T I T L E')
>>>
>>> t.title
['G A M E', 'T I T L E']

```
#### add_banner_line()
Adds a string item to be rendered as a line of text in the banner.

```python
>>> t.add_banner_line("This is a banner!")
>>> t.add_banner_line("Where you can put your game tagline.")
>>>
>>> t.bannerText
['This is a banner!', 'Where you can put your game tagline.']
```

#### add_menu_item()
Can take a string or a list of strings and add it to the menu list. 

```python
>>> t.add_menu_item(["Continue", "New Game", "Settings", "Quit", "Menu Item", "Another Menu Item"])
>>> t.menu
['Continue', 'New Game', 'Settings', 'Quit', 'Menu Item', 'Another Menu Item']
```
#### render_title()
If the title is not empty, renders only the title in stylized ascii art.

```python
>>> t.color = "green"
>>> t.render_title()
```
![render_title](images/render_title.png)

#### render_banner()
If the banner is not empty, will render the banner text in a banner drawn with '*'
Each list item is rendered as a line, and the lines are centered in the banner.

```python
t.bannerColor = "blue"
t.render_banner()
```
![render_banner](images/render_banner.png)
#### render_menu()
If the menu list is not empty, will render the menu in columns (default 3 columns). This function does not create functionality for the menu and only displays it.

```python
>>> t.render_menu()
```
![render_menu](images/render_menu.png)
#### render_title_screen()
This function will render a formatted title screen with the Title rendered at top, then the caption, then the banner and finally the menu. If any of those objects are empty, it will skip rendering it. This function only displays the title screen and does not add any functionality.

```python
    from modules.tagesplash import TitleScreen

    # Add Title Screen Text
    t = TitleScreen()
    t.add_title_line("G A M E")
    t.add_title_line("T I T L E")
    # Set Title Screen Text Color
    t.color = "green"
    # Add Caption
    t.caption = "Version 0.1alpha(DEMO)"
    # Add Banner Text
    t.add_banner_line("This is a banner!")
    t.add_banner_line("Where you can put your game tagline.")
    # Set Banner Color
    t.bannerColor = "blue"
    # Add Title Screen Menu
    t.add_menu_item(["Continue", "New Game", "Settings", "Quit", "Menu Item", "Another Menu Item"])
    # Render Title Screen
    t.render_title_screen()
```
![title_screen](images/title_screen.png)

# module::tageutils
## function::clearScreen()
OS independed method of clearing the console.

## function::transfer_item(item, fromObj, toObj)
Transfers an inventory item between two(2) objects with an inventory

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

# Transfer item from the MapTile to the Player
transfer_item(i, m, p)

# Check m and p for item in inventory
m.check_item("test item")
'False'

p.check_item("test item")
'True'
```

## class::StateMachine()
```python
from modules.tageutils import StateMachine
```
Class that impliments a Finite State Machine. Currently used as a parent class to [TextParser](#classtextparser). FSMs can be useful in a veriety of situations, like setting that current state of a player, enemey, or MapTile.
<!---Need to add a section to documentation explaining what a Finite State Machine is --->

### Class Variables

#### handlers
*dict*

Dictionary object that holds handlers for each state, with the name of each state as a dictionary key.

**Default Value: {}**

#### startState
*str*

String Object that holds the name of the state to use as the starting condition for the finite state machine

**Default Value: `None`**

#### endStates
*list*

List of state names that are end states (No transition to another state available). 

**Default Value: []**

### Class Functions

#### add_state(name, handler)
Adds a state and handler to the Finite State Machine. Handlers must be defined seperately as functions, See (State Transition Definition)[#state_transition_definition] for information on creating state transitions. By default, states will not be set as an end_state. To set an endstate add `end_state=1` after the handler.

```python
from modules.tageutils import StateMachine

s = StateMachine()
s.add_state('start', start_transition)
s.add_state('another_state', another_state_transition)
```

#### set_start(name)
Takes the name of the start state for the state machine. 

```python
...
s.set_start('start')
```

#### run(cargo)

Runs the finite state machine recursevly with cargo being the initial condition. Run will exit when it hits an end state.

```python
...
s.run("This text is the cargo")
```

## State Transition Definition
<!---I need to add a section on defining state transition's here --->
# module::tageparse

## class::TextParser