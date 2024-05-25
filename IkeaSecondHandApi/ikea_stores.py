import requests
from sqlalchemy import select
from sqlalchemy.orm import Session
from IkeaSecondHandApi import local_constants
from models.countries import Countries
from utils import database_handler


def getStoreIds(country_constants=["nl/nl"]):
    stores = []
    for country in country_constants:
        request_url = f"https://www.ikea.com/{country}/meta-data/navigation/stores.json"
        response = requests.get(request_url)

        for store in response.json():
            stores.append({"id": store["id"], "name": store["name"], "display_name": store["displayName"], "country": country})
    
    return stores

def getAvailableCountries():
    countries = []
    engine = database_handler.getDatabaseEngine()
    
    with Session(engine) as session:
        stmt = select(Countries)

    for r in session.execute(stmt):
        countries.append({"id": r.Countries.locale, "name": r.Countries.display_name})

    return countries
