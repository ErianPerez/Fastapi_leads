from fastapi import FastAPI
from app.database import engine, init_db
from app.models import Base
from app.endpoints import leads, subjects

app = FastAPI()

Base.metadata.create_all(bind=engine)
@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(leads.router_leads)
app.include_router(subjects.router_subjects)