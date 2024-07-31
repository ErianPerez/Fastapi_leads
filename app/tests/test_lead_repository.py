import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.lead import Base, Lead
from app.models.subject import Subject
from app.crud.lead_repository import LeadRepository
from pydantic import ValidationError
from app.schemas.lead import LeadCreate

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

@pytest.fixture
def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_get_leads(db):
    repo = LeadRepository(db)
    db.query(Lead).delete()
    db.query(Subject).delete()
    db.commit()
    
    lead_data = LeadCreate(
        name="Another Test Lead",
        email="another@example.com",
        address="Another Address",
        phone="0987654321",
        registration_year=2024,
        subjects=[]
    )
    created_lead = repo.create_lead(lead_data)
    
    print("Created Lead:", created_lead.name)
    
    leads = repo.get_leads()
    for lead in leads:
        print("Lead in DB:", lead.name)

    assert len(leads) > 0
    assert leads[0].name == "Another Test Lead"


def test_create_lead_with_subjects(db):
    repo = LeadRepository(db)
    lead_data = LeadCreate(
        name="Lead with Subjects",
        email="with_subjects@example.com",
        address="Subject Address",
        phone="2345678901",
        registration_year=2024,
        subjects=[
            {
                "name": "Subject 1",
                "career": "Career A",
                "duration": 10,
                "registration_year": 2024,
                "times_taken": 1
            },
            {
                "name": "Subject 2",
                "career": "Career B",
                "duration": 15,
                "registration_year": 2024,
                "times_taken": 2
            }
        ]
    )
    lead = repo.create_lead(lead_data)
    
    assert lead.name == "Lead with Subjects"
    
    subjects = db.query(Subject).filter(Subject.lead_id == lead.id).all()
    assert len(subjects) == 2
    assert subjects[0].name == "Subject 1"
    assert subjects[1].name == "Subject 2"

def test_get_lead_by_id(db):
    repo = LeadRepository(db)
    lead_data = LeadCreate(
        name="Lead to Find",
        email="find@example.com",
        address="Find Address",
        phone="3456789012",
        registration_year=2024,
        subjects=[]
    )
    lead = repo.create_lead(lead_data)

    found_lead = repo.get_lead(lead.id)
    assert found_lead is not None
    assert found_lead.name == "Lead to Find"

def test_delete_lead(db):
    repo = LeadRepository(db)
    lead_data = LeadCreate(
        name="Lead to Delete",
        email="delete@example.com",
        address="Delete Address",
        phone="4567890123",
        registration_year=2024,
        subjects=[]
    )
    lead = repo.create_lead(lead_data)
    
    db.query(Lead).filter(Lead.id == lead.id).delete()
    db.commit()

    deleted_lead = repo.get_lead(lead.id)
    assert deleted_lead is None

def test_create_lead_invalid_data(db):
    repo = LeadRepository(db)
    try:
        lead_data = LeadCreate(
            name="",  # Nombre vacío es inválido
            email="invalid@example.com",
            address="Invalid Address",
            phone="5678901234",
            registration_year=2024,
            subjects=[]
        )
        assert False, "Expected a ValidationError for invalid data"
    except ValidationError as e:
        assert "string_too_short" in str(e) 
    except Exception as e:
        assert False, f"Unexpected exception type: {type(e).__name__}"