from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.lead import LeadCreate, Lead
from app.database import database
from app.crud.lead_repository import LeadRepository

router_leads = APIRouter()

@router_leads.post("/leads/", response_model=Lead)
def create_lead(lead: LeadCreate, db: Session = Depends(database.get_db)) -> Lead:
    """
    Create a new lead with the given data.

    Args:
        lead (LeadCreate): The data of the lead to be created.
        db (Session): The database session dependency.

    Returns:
        Lead: The created lead with an assigned ID.
    """
    repo = LeadRepository(db)
    return repo.create_lead(lead=lead)

@router_leads.get("/leads/", response_model=List[Lead])
def read_leads(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)) -> List[Lead]:
    """
    Retrieve a list of leads with optional pagination.

    Args:
        skip (int): The number of items to skip.
        limit (int): The maximum number of items to return.
        db (Session): The database session dependency.

    Returns:
        List[Lead]: A list of leads.
    """
    repo = LeadRepository(db)
    leads = repo.get_leads(skip=skip, limit=limit)
    return leads

@router_leads.get("/leads/{lead_id}", response_model=Lead)
def read_lead(lead_id: int, db: Session = Depends(database.get_db)) -> Lead:
    """
    Retrieve a lead by its ID.

    Args:
        lead_id (int): The ID of the lead to retrieve.
        db (Session): The database session dependency.

    Raises:
        HTTPException: If the lead is not found.

    Returns:
        Lead: The lead with the given ID.
    """
    repo = LeadRepository(db)
    db_lead = repo.get_lead(lead_id=lead_id)
    if db_lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    return db_lead