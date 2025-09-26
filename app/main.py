from fastapi import FastAPI
from datetime import datetime, timedelta
from fastapi.concurrency import asynccontextmanager
from sqlmodel import Session, SQLModel, select

from app.core.database import engine
from app.models.campaign import Campaign
from app.api.campaigns import router as campaigns_router


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    # Add sample data if database is empty
    with Session(engine) as session:
        if not session.exec(select(Campaign)).first():
            session.add_all([
                Campaign(name="Summer Launch", due_date=datetime.now() + timedelta(days=30)),
                Campaign(name="Black Friday", due_date=datetime.now() + timedelta(days=60)),
                Campaign(name="Holiday Sale", due_date=datetime.now() + timedelta(days=90)),
                Campaign(name="Spring Promo", due_date=datetime.now() + timedelta(days=120)),
                Campaign(name="Back to School", due_date=datetime.now() + timedelta(days=150)),
                Campaign(name="Winter Clearance", due_date=datetime.now() + timedelta(days=180)),
            ])
            session.commit()
    yield


app = FastAPI(
    title="OmniCopy Campaign API",
    description="A FastAPI application for managing marketing campaigns",
    version="1.0.0",
    root_path="/api/v1",
    lifespan=lifespan
)


@app.get("/")
async def read_root():
    return {"message": "OmniCopy Campaign API is running", "version": "1.0.0"}


# Include routers
app.include_router(campaigns_router)