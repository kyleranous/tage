import unittest
from modules.tageplayer import *
from modules.tageitem import *

class test_player(unittest.TestCase):
    
    def test_creation(self):

        with self.subTest():
            with self.assertRaises(ValueError):
                p = Player(100)
        
        with self.subTest():
            p = Player("Test")
            self.assertTrue(p.has_inventory())


    def test_inventory(self):
        p = Player("Test")
        i = Item("Test Item", "test item", 100)

        # Check that item can be added to inventory
        with self.subTest():
            p.add_item(i,1)
            self.assertTrue(p.check_item(i.name))
            self.assertTrue(p.inventory[i.name.lower()]["qty"]==1)

        # Check that additional items will incriment qty
        with self.subTest():
            p.add_item(i, 1)
            self.assertTrue(p.inventory[i.name.lower()]["qty"]==2)
        
        # Check that items not in inventory return false
        with self.subTest():
            i2 = Item("Another Item", "Yet another item", 200)
            self.assertFalse(p.check_item(i2.name))

        # Check that items can be removed from inventory
        with self.subTest():
            p.remove_item(i.name)
            self.assertFalse(p.check_item(i.name))


    def test_player_pos(self):
        p = Player("Test")
        # Add Tests here - Test functions must start with test_ to run
        with self.subTest():
            self.assertEqual(p.player_pos(), [0,0])

        # Check update_pos working
        with self.subTest():
            p.update_pos(1,0)
            self.assertEqual(p.player_pos(), [1,0])
            

            p.update_pos(0,1)
            self.assertEqual(p.player_pos(), [1,1])
            

            p.update_pos(-1,0)
            self.assertEqual(p.player_pos(), [0,1])

            p.update_pos(0,-1)
            self.assertEqual(p.player_pos(), [0,0])
            