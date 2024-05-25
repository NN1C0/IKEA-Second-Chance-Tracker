from sqlalchemy import create_engine, text, select
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.orm import Session
import configparser

from utils import database_handler
from IkeaSecondHandApi import ikea_stores, second_chance_search

from models.countries import Countries
from models.stores import Stores
from models.offers import Offers

def main():
    updateStoresInDatabase()


def updateStoresInDatabase():
    countries = ikea_stores.getAvailableCountries()
    engine = database_handler.getDatabaseEngine()

    with Session(engine) as session:
        session.execute(text("TRUNCATE TABLE offers"))
        for c in countries:
            stores = ikea_stores.getStoreIds([c["id"]])
            country_id_stmt = select(Countries.id).where(Countries.locale == c["id"])
            country_id = session.execute(country_id_stmt).first()
            
            for s in stores:
                insert_stmt = insert(Stores).values(store_id=s["id"],
                                                    country=country_id[0],
                                                    name=s["name"],
                                                    display_name = s["display_name"])
                on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
                    store_id=insert_stmt.inserted.store_id
                )
                session.execute(on_duplicate_key_stmt)

            updateArticlesInDatabase(session, c["id"], stores)
            session.commit()

def updateArticlesInDatabase(session, country_locale, stores):
    store_ids = [s["id"] for s in stores]
    products = second_chance_search.searchSecondChance("", country_locale, store_ids, debug=True)
    session.execute(insert(Offers), products)


if __name__ == "__main__":
    main()