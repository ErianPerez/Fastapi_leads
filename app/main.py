from fastapi import FastAPI
from app.database import database
from app.endpoints import leads, subjects
from app.models.lead import Lead  
from app.models.subject import Subject

app = FastAPI()

@app.on_event("startup")
def on_startup() -> None:
    """
    Event handler that initializes the database on application startup.
    """
    database.init_db()
    database.Base.metadata.create_all(bind=database.engine)

@app.get("/", tags=["Home"])
def read_root():
    """
    Welcome endpoint that provides information about the API.
    """
    return {
        "message": "Welcome to the Leads API!",
        "description": "This API allows you to manage leads and subjects.",
        "endpoints": {
            "/api/leads": "Operations related to leads.",
            "/api/subjects": "Operations related to subjects."
        }
    }

app.include_router(leads.router_leads, prefix="/api", tags=["Leads"])
app.include_router(subjects.router_subjects, prefix="/api", tags=["Subjects"])