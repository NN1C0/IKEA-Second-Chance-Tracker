import os, dotenv

ENV = os.getenv("ENV", 'dev')
if ENV == 'dev':
    dotenv.load_dotenv()

DEBUG = os.getenv("DEBUG", 'False')
DATABASE_URL = os.getenv("DATABASE_URL")
if "postgres" in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")
