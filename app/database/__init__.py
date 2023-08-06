# app/database/__init__.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace the SQLALCHEMY_DATABASE_URL with your actual database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./users.db"

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory for interacting with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
