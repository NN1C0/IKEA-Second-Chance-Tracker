import logging
from sqlalchemy import create_engine
from Config.config import DATABASE_URL

def getDatabaseEngine():
    try:
        engine = create_engine(get_database_uri())
        return engine
    except Exception as e:
        logging.exception(e)
        return None

def get_database_uri() -> str:
    return DATABASE_URL