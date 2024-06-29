import configparser, dotenv, os
from sqlalchemy import create_engine
from Config.config import DATABASE_URL

def getDatabaseEngine():
    return create_engine(get_database_uri())

def get_database_uri() -> str:
    return DATABASE_URL