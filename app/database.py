from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator
import os

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/leads_db")
        self.engine = create_engine(self.DATABASE_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()

    def init_db(self):
        """Create all tables in the database."""
        self.Base.metadata.create_all(bind=self.engine)

    def get_db(self) -> Generator[sessionmaker, None, None]:
        """Provide a transactional database session."""
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

database = Database()
