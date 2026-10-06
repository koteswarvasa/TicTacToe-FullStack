import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base


# Load .env
load_dotenv()


# ==============================
# Database Configuration
# ==============================

DB_SERVER = os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME")
DB_DRIVER = os.getenv(
    "DB_DRIVER",
    "ODBC Driver 18 for SQL Server"
)

DB_TRUSTED_CONNECTION = os.getenv(
    "DB_TRUSTED_CONNECTION",
    "yes"
)


# ==============================
# Connection String
# ==============================

DATABASE_URL = (
    f"mssql+pyodbc://@"
    f"{DB_SERVER}/"
    f"{DB_NAME}"
    f"?driver={DB_DRIVER.replace(' ', '+')}"
    f"&trusted_connection={DB_TRUSTED_CONNECTION}"
    f"&TrustServerCertificate=yes"
)


# ==============================
# SQLAlchemy Engine
# ==============================

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)


# ==============================
# Session
# ==============================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ==============================
# Base
# ==============================

Base = declarative_base()


# ==============================
# Database Dependency
# ==============================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ==============================
# Test Connection
# ==============================

def test_connection():

    try:

        with engine.connect() as connection:

            result = connection.execute(
                text("SELECT 1")
            )

            print(
                "Database connection successful!"
            )

            print(
                "Result:",
                result.scalar()
            )

    except Exception as e:

        print(
            "Database connection failed!"
        )

        print(e)


if __name__ == "__main__":

    test_connection()