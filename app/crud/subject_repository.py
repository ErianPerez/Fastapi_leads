from sqlalchemy.orm import Session
from app.models.subject import Subject
from app.schemas.subject import SubjectCreate

class SubjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_subject(self, subject: SubjectCreate):
        db_subject = Subject(**subject.dict())
        self.db.add(db_subject)
        self.db.commit()
        self.db.refresh(db_subject)
        return db_subject

    def get_subjects(self, skip: int = 0, limit: int = 10):
        return self.db.query(Subject).offset(skip).limit(limit).all()

    def get_subject(self, subject_id: int):
        return self.db.query(Subject).filter(Subject.id == subject_id).first()
