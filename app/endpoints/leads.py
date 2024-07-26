from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas import LeadCreate, Lead
from app.database import get_db
from app import crud

router_leads = APIRouter()

@router_leads.post("/leads/", response_model=Lead)
def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    return crud.create_lead(db=db, lead=lead)

@router_leads.get("/leads/", response_model=List[Lead])
def read_leads(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    leads = crud.get_leads(db, skip=skip, limit=limit)
    return leads

@router_leads.get("/leads/{lead_id}", response_model=Lead)
def read_lead(lead_id: int, db: Session = Depends(get_db)):
    db_lead = crud.get_lead(db, lead_id=lead_id)
    if db_lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    return db_lead