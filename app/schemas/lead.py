from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from .subject import SubjectCreate, Subject

class LeadBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    address: Optional[str] = None
    phone: Optional[str] = None
    registration_year: Optional[int] = None

    class Config:
        from_attributes = True  

class LeadCreate(LeadBase):
    subjects: List[SubjectCreate] = []

class Lead(LeadBase):
    id: int
    subjects: List[Subject] = []
