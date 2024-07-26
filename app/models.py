from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Lead(Base):
    __tablename__ = "leads"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    address = Column(String)
    phone = Column(String)
    registration_year = Column(Integer)
    
    subjects = relationship("Subject", back_populates="lead")

class Subject(Base):
    __tablename__ = "subjects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    career = Column(String, index=True)
    duration = Column(Integer)  # Duración en semanas
    registration_year = Column(Integer)
    times_taken = Column(Integer)
    lead_id = Column(Integer, ForeignKey("leads.id"))
    
    lead = relationship("Lead", back_populates="subjects")