import unittest
from tagemap import MapTile
from tage_items import Item


class test_map_tile(unittest.TestCase):    
    
    def test_tile_creation(self):
        m = MapTile("Test Tile")
        self.assertEqual(m.name, "Test Tile")
        
    def test_manipulate_item(self):
        i = Item("Test Item", "This is a test item", 0)
        m = MapTile("Test Tile")
        m.add_item(i, 1)

        with self.subTest():
            self.assertEqual(m.map_items[i.name.lower()]["item"], i, "Item was not added to tile inventory correctly")
        
        with self.subTest():
            m.remove_item(i.name)
            self.assertFalse(m.map_items)

    def test_check_item(self):
        i = Item("Test Item", "This is a test item", 0)
        m = MapTile("Test Tile")
        m.add_item(i, 1)

        with self.subTest():
            self.assertTrue(m.check_item(i.name))

        with self.subTest():
            self.assertFalse(m.check_item("FAKE ITEM"))

    def test_custom_spawn_rate(self):
        m = MapTile("Test Tile")
        # Passing custom spawn rates that are greater then 1
        m.set_spawn_rate(.5,.5,.3,.2,.2)

        #Test that sum of custom spawn rates was converted to 1
        with self.subTest():
            rateTotal = m.commonRate \
                        + m.uncommonRate \
                        + m.rareRate \
                        + m.ultraRareRate \
                        + m.noSpawnRate
            self.assertEqual(rateTotal, 1.0)

        #Test that common and uncommon spawn rates are equal
        with self.subTest():
            self.assertEqual(m.commonRate, m.uncommonRate)

        #Test that ultra-rare and noSpawn rates are equal
        with self.subTest():
            self.assertEqual(m.ultraRareRate, m.noSpawnRate)