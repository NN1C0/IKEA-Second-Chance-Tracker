import unittest
from IkeaSecondHandApi.ikea_stores import getAvailableCountries


from IkeaSecondHandApi.ikea_stores import getAvailableCountries, getStoreIds

class TestIkeaStores(unittest.TestCase):

    def test_getAvailableCountries(self):
        countries = getAvailableCountries()
        self.assertIn(countries[0], [{'id': 'de/de', 'name': 'Germany'}])

    def test_getStoreIds(self):
        store_ids = getStoreIds(['de/de'])
        self.assertGreater(len(store_ids), 0)