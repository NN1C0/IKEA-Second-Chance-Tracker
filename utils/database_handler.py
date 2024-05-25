import configparser
from sqlalchemy import create_engine

def getDatabaseEngine():
    config = configparser.ConfigParser()
    config.read("config/credentials.ini")
    db_host = config["Database"]["db_host"]
    db_user = config["Database"]["db_user"]
    db_password = config["Database"]["db_password"]


    return create_engine(f"mysql://{db_user}:{db_password}@{db_host}:3306/ikea_second_chance")