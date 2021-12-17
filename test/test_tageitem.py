import unittest
from modules.tageitem import *


class test_item(unittest.TestCase):
    
    def test_creation(self):
        
        with self.subTest():
            with self.assertRaises(TypeError):
                i = Item(100, "Test", 100)

        with self.subTest():
            with self.assertRaises(TypeError):
                i = Item("Test", 100, 100)
        
        with self.subTest():
            with self.assertRaises(TypeError):
                i = Item("Test", "Test", "100")
    
        with self.subTest():
            i = Item("Test", "test", 100)
            self.assertTrue(i.is_item())