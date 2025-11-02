import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://warehouse_user:warehouse_pass@localhost:5432/warehouse_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False