from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.subject import SubjectCreate, Subject
from app.database import database
from app.crud.subject_repository import SubjectRepository

router_subjects = APIRouter()

@router_subjects.post("/subjects/", response_model=Subject)
def create_subject(subject: SubjectCreate, db: Session = Depends(database.get_db)) -> Subject:
    """
    Create a new subject with the given data.

    Args:
        subject (SubjectCreate): The data of the subject to be created.
        db (Session): The database session dependency.

    Returns:
        Subject: The created subject with an assigned ID.
    """
    repo = SubjectRepository(db)
    return repo.create_subject(subject=subject)

@router_subjects.get("/subjects/", response_model=List[Subject])
def read_subjects(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)) -> List[Subject]:
    """
    Retrieve a list of subjects with optional pagination.

    Args:
        skip (int): The number of items to skip.
        limit (int): The maximum number of items to return.
        db (Session): The database session dependency.

    Returns:
        List[Subject]: A list of subjects.
    """
    repo = SubjectRepository(db)
    subjects = repo.get_subjects(skip=skip, limit=limit)
    return subjects

@router_subjects.get("/subjects/{subject_id}", response_model=Subject)
def read_subject(subject_id: int, db: Session = Depends(database.get_db)) -> Subject:
    """
    Retrieve a subject by its ID.

    Args:
        subject_id (int): The ID of the subject to retrieve.
        db (Session): The database session dependency.

    Raises:
        HTTPException: If the subject is not found.

    Returns:
        Subject: The subject with the given ID.
    """
    repo = SubjectRepository(db)
    db_subject = repo.get_subject(subject_id=subject_id)
    if db_subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")
    return db_subject
