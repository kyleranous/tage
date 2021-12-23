import unittest
import os
from modules.tagemap import *
from modules.tageitem import Item



class test_game_map(unittest.TestCase):

    def test_map_creation(self):
        g = GameMap("Test Map")

        self.assertEqual(g.name, 'Test Map')
        self.assertEqual(g.tileMat, [])

    def test_map_import(self):
        g = GameMap("Test Map")
        path = os.path.dirname(__file__)
        filename = os.path.join(path, 'assets/mapTest.csv')
        g.readMapFile(filename)
        self.assertTrue(len(g.tileMat) == 6)
        self.assertTrue(len(g.tileMat[0]) == 6)
        self.assertEqual(g.tileMat[0][0], 'Tile 00')
        self.assertEqual(g.tileMat[5][5], 'Tile 55')
        self.assertEqual(g.tileMat[3][2], 'Tile 32')
        self.assertFalse(g.tileMat[1][1] == 'Tile 22')

        
class test_map_tile(unittest.TestCase):    
    
    def test_tile_creation(self):
        m = MapTile("Test Tile")
        self.assertEqual(m.name, "Test Tile")
        
    def test_manipulate_item(self):
        i = Item("Test Item", "This is a test item", 0)
        m = MapTile("Test Tile")
        m.add_item(i, 1)

        with self.subTest():
            self.assertEqual(m.mapItems[i.name.lower()]["item"], i, "Item was not added to tile inventory correctly")
        
        with self.subTest():
            m.remove_item(i.name)
            self.assertFalse(m.mapItems)


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