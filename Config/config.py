import os, dotenv

ENV = os.getenv("ENV", 'dev')
if ENV == 'dev':
    dotenv.load_dotenv()

DEBUG = os.getenv("DEBUG", 'False')
DATABASE_URL = os.getenv("DATABASE_URL")
