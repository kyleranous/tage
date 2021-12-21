import unittest
from modules.tageparse import TextParser


class test_parse(unittest.TestCase):

    def test_manipulation_parse(self):
        t = TextParser()

        # Test Take Item Path
        with self.subTest():
            response = t.parse_text("Pick Up Item")
            self.assertEqual(response, ['TAKE', 'ITEM', ''])

        with self.subTest():
            response = t.parse_text("Pick up test item")
            self.assertEqual(response, ['TAKE', 'TEST ITEM', ''])

        with self.subTest():
            response = t.parse_text("take item")
            self.assertEqual(response, ['TAKE', 'ITEM', ''])

        with self.subTest():
            response = t.parse_text("take test item")
            self.assertEqual(response, ['TAKE', 'TEST ITEM', ''])

        # Test Drop Item Path
        with self.subTest():
            response = t.parse_text("drop item")
            self.assertEqual(response, ['DROP', 'ITEM', ''])
        
        with self.subTest():
            response = t.parse_text("drop test item")
            self.assertEqual(response, ['DROP', 'TEST ITEM', ''])

        with self.subTest():
            response = t.parse_text("put down item")
            self.assertEqual(response, ['DROP', 'ITEM', ''])
        
        with self.subTest(): # Need to add support for this syntax
            response = t.parse_text("put item down")
            self.assertEqual(response, ['ERROR'])
        
        with self.subTest():
            response = t.parse_text("put down test item")
            self.assertEqual(response, ['DROP', 'TEST ITEM', ''])

        # Test Store Item Path
        with self.subTest():
            response = t.parse_text("put away item")
            self.assertEqual(response, ['STOW', 'ITEM', ''])

        with self.subTest(): # Need to add support for this syntax
            response = t.parse_text("put item away")
            self.assertEqual(response, ['ERROR'])
        
        with self.subTest():
            response = t.parse_text("store item")
            self.assertEqual(response, ['STOW', 'ITEM', ''])


    def test_inspection_states(self):
        
        t = TextParser()
        with self.subTest():
            response = t.parse_text("inspect item")
            self.assertEqual(response, ['INSPECT', 'ITEM', ''])
        
        with self.subTest():
            response = t.parse_text("look at item")
            self.assertEqual(response, ['INSPECT', 'ITEM', ''])

        with self.subTest():
            response = t.parse_text("look in bag")
            self.assertEqual(response, ['INSPECT', 'BAG', 'IN'])

        with self.subTest():
            response = t.parse_text("check out the window")
            self.assertEqual(response, ['INSPECT', 'WINDOW', 'OUT'])

    
    def test_movement_states(self):
        pass


    def test_invalid_input(self):
        # Test a response I know will present an error
        t = TextParser()
        response = t.parse_text("Play that funky music, white boy")
        self.assertEqual(response, ['ERROR'])
