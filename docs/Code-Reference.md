## Classes

### GameMap()
*Module: tage_map*

### MapTile()
*Module: tage_map*

**Class Functions**:

### StartTile()
*Module: tage_map*
*Extends [MapTile()](#maptile())*

**Class Functions**:

### TitleScreen()

#### Class Variables
* title
* titleFont
* width
* color
* bannerText
* bannerColor
* caption
* menu

#### Class Functions:
**add_title_line(title)**

**add_banner_line(bannerText)**

**add_menu_item(menuItem)**

**render_title()**

**render_menu()**

**render_title_screen()**

##### ex:
![title_screen](images/title_screen.png)
## Modules

### tageutils
#### clearScreen()
OS independed method of clearing the console

#### transfer_item(item, fromObj, toObj)
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