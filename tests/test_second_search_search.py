import unittest

from IkeaSecondHandApi import second_chance_search

#Testing with real store and country. The chance of not having ANY second chance items is too low to be relevant.
class TestSecondChanceSearch(unittest.TestCase):
    def test_searchSecondChance(self):
        found_items = second_chance_search.searchSecondChance('', 'de/de', ['066'])
        self.assertGreater(len(found_items), 0)

    def test_searchLocalDatabase(self):
        found_items = second_chance_search.searchLocalDatabase('', ['066'])
        self.assertGreater(len(found_items), 0)