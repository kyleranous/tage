from tage_map import MapTile
from tage_items import Item

m = MapTile("Test Tile")
c = Item("Common Item", "This is a common item.", 0)
u = Item("Uncommon Item", "This is an uncommon item.", 0)
r = Item("Rare Item", "This is a rare item.", 0)
ur = Item("Ultra-Rare Item", "This is an ultra-rare item", 0)

m.add_spawn_item(c, 1)
m.add_spawn_item(u, 2)
m.add_spawn_item(r, 3)
m.add_spawn_item(ur, 4)

for x in range(0,1000):
    m.spawn_item()

print(m.map_items)
