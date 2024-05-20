import requests
from IkeaSecondHandApi import local_constants


def getStoreIds(country_constants=["nl/nl"]):
    stores = []
    for country in country_constants:
        request_url = f"https://www.ikea.com/{country}/meta-data/navigation/stores.json"
        response = requests.get(request_url)

        for store in response.json():
            stores.append({"id": store["id"], "name": store["name"], "country": country})
    
    return stores

def getAvailableCountries():
    countries = []
    for l in local_constants.LocalConstants:
        countries.append({"id": l.value, "name": l.name})
    return countries