import unittest

from IkeaSecondHandApi import second_chance_search

class TestSecondChanceSearch(unittest.TestCase):
    def test_searchSecondChance(self):
        found_items = second_chance_search.searchSecondChance('', 'de/de', ['066'])
        self.assertGreater(len(found_items), 0)