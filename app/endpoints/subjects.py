from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas import SubjectCreate, Subject
from app.database import get_db
from .. import crud

router_subjects = APIRouter()

@router_subjects.post("/subjects/", response_model=Subject)
def create_subject(subject: SubjectCreate, db: Session = Depends(get_db)):
    return crud.create_subject(db=db, subject=subject)

@router_subjects.get("/subjects/", response_model=List[Subject])
def read_subjects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    subjects = crud.get_subjects(db, skip=skip, limit=limit)
    return subjects

@router_subjects.get("/subjects/{subject_id}", response_model=Subject)
def read_subject(subject_id: int, db: Session = Depends(get_db)):
    db_subject = crud.get_subject(db, subject_id=subject_id)
    if db_subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")
    return db_subject