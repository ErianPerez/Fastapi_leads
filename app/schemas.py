from pydantic import BaseModel
from typing import List, Optional

class SubjectBase(BaseModel):
    name: str
    career: str
    duration: Optional[int] = None
    registration_year: Optional[int] = None
    times_taken: Optional[int] = None

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int
    lead_id: int

    class Config:
        from_attributes = True  

class LeadBase(BaseModel):
    name: str
    email: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    registration_year: Optional[int] = None

class LeadCreate(LeadBase):
    subjects: List[SubjectCreate] = []

class Lead(LeadBase):
    id: int
    subjects: List[Subject] = []

    class Config:
        from_attributes = True