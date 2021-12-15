import unittest
from modules.tageutils import *
from modules.tageitem import Item
from modules.tageplayer import Player
from modules.tagemap import MapTile


class test_tageutils(unittest.TestCase):
    """ Tests utility functions """

    def test_transfer_item(self):
        """ Tests the transfer of items between 2 inventories"""
        self.i = Item("Test Item", "This is a test item", 0)
        self.m = MapTile("Test Tile")
        self.p = Player("Test Player 1")
        self.p2 = Player("Test Player 2")

        # Test Player -> Map (Simulating Drop Item)
        with self.subTest():
            self.p.add_item(self.i, 1)
            transfer_item(self.i.name, self.p, self.m)

            self.assertTrue(self.m.check_item(self.i.name))
            self.assertFalse(self.p.check_item(self.i.name))

        # Test Map -> Player (Simulating Picking up Item)
        with self.subTest():
            transfer_item(self.i.name, self.m, self.p)

            self.assertTrue(self.p.check_item(self.i.name))
            self.assertFalse(self.m.check_item(self.i.name))

        # Test Player -> Player (Simulating P2P Transfer)
        with self.subTest():
            transfer_item(self.i.name, self.p, self.p2)

            self.assertTrue(self.p2.check_item(self.i.name))
            self.assertFalse(self.p.check_item(self.i.name))
