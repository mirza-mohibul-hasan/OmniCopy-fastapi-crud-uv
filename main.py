from fastapi import FastAPI
from datetime import datetime, timedelta
from typing import Any
app = FastAPI(root_path="/api/v1")


@app.get("/")
async def read_root():
    return {"message": "Server is running"}

"""
Campaigns
- campaign_id: int
- name: str
- due_date: str
- created_at: str
"""
data: Any = [
    {
        "campaign_id": 1,
        "name": "Summer Launch",
        "due_date": datetime.now(),
        "created_at": datetime.now() + timedelta(days=-30)
    },
    {
        "campaign_id": 2,
        "name": "Black Friday",
        "due_date": datetime.now(),
        "created_at": datetime.now() + timedelta(days=-30)
    },
]


@app.get("/campaigns")
async def read_campaigns():
    return {"campaigns": data}
