from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import database

Base = database.Base

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

    def __repr__(self):
        return f"<Subject(id={self.id}, name='{self.name}', career='{self.career}')>"
