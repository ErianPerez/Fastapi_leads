from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import database

Base = database.Base

class Lead(Base):
    __tablename__ = "leads"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False ,index=True)
    email = Column(String, unique=True, index=True)
    address = Column(String)
    phone = Column(String)
    registration_year = Column(Integer)
    
    subjects = relationship("Subject", back_populates="lead")

    def __repr__(self):
        return f"<Lead(id={self.id}, name='{self.name}', email='{self.email}')>"
