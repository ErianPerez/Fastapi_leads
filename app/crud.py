from sqlalchemy.orm import Session
from app.models import Lead, Subject
from app.schemas import LeadCreate, SubjectCreate

def create_lead(db: Session, lead: LeadCreate):
    db_lead = Lead(
        name=lead.name,
        email=lead.email,
        address=lead.address,
        phone=lead.phone,
        registration_year=lead.registration_year
    )
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    
    for subject in lead.subjects:
        db_subject = Subject(
            name=subject.name,
            career=subject.career,
            duration=subject.duration,
            registration_year=subject.registration_year,
            times_taken=subject.times_taken,
            lead_id=db_lead.id
        )
        db.add(db_subject)
    
    db.commit()
    return db_lead

def get_leads(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Lead).offset(skip).limit(limit).all()

def get_lead(db: Session, lead_id: int):
    return db.query(Lead).filter(Lead.id == lead_id).first()

def create_subject(db: Session, subject: SubjectCreate):
    db_subject = Subject(**subject.dict())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

def get_subjects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Subject).offset(skip).limit(limit).all()

def get_subject(db: Session, subject_id: int):
    return db.query(Subject).filter(Subject.id == subject_id).first()