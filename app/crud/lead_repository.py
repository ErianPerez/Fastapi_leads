from sqlalchemy.orm import Session
from app.models.lead import Lead
from app.models.subject import Subject
from app.schemas.lead import LeadCreate

class LeadRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_lead(self, lead: LeadCreate):
        db_lead = Lead(
            name=lead.name,
            email=lead.email,
            address=lead.address,
            phone=lead.phone,
            registration_year=lead.registration_year
        )
        self.db.add(db_lead)
        self.db.commit()
        self.db.refresh(db_lead)
        
        for subject in lead.subjects:
            db_subject = Subject(
                name=subject.name,
                career=subject.career,
                duration=subject.duration,
                registration_year=subject.registration_year,
                times_taken=subject.times_taken,
                lead_id=db_lead.id
            )
            self.db.add(db_subject)
        
        self.db.commit()
        return db_lead

    def get_leads(self, skip: int = 0, limit: int = 10):
        return self.db.query(Lead).offset(skip).limit(limit).all()

    def get_lead(self, lead_id: int):
        return self.db.query(Lead).filter(Lead.id == lead_id).first()
