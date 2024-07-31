from pydantic import BaseModel
from typing import Optional

class SubjectBase(BaseModel):
    name: str
    career: str
    duration: Optional[int] = None
    registration_year: Optional[int] = None
    times_taken: Optional[int] = None

    class Config:
        from_attributes = True

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int
    lead_id: int
