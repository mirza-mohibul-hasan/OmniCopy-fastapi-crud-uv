from fastapi import FastAPI, HTTPException, Response
from datetime import datetime, timedelta
from typing import Any
from random import randint
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

@app.get("/campaigns/{id}")
async def read_campaign(id: int):
    for campaign in data:
        if campaign.get("campaign_id") == id:
            return {"campaign" : campaign}
    raise HTTPException(status_code=404, detail="Campaign not found")

@app.post("/campaigns", status_code=201)
async def create_campaign(body: dict[str, Any]):
    new: Any = {
        "campaign_id": randint(3, 10000),
        "name": body.get("name"),
        "due_date": body.get("due_date"),
        "created_at": datetime.now() + timedelta(days=-30)
    }
    data.append(new)
    return {"campaign": new}

@app.put("/campaigns/{id}")
async def update_campaign(id: int, body: dict[str, Any]):
    for index, campaign in enumerate(data):
        if campaign.get("campaign_id") == id:
            updated: Any = {
                "campaign_id": id,
                "name": body.get("name"),
                "due_date": body.get("due_date"),
                "created_at": campaign.get("created_at")
            }
            data[index] = updated
            return {"campaign": updated}
    raise HTTPException(status_code=404, detail="Campaign not found")

@app.delete("/campaigns/{id}")
async def delete_campaign(id: int):
    for index, campaign in enumerate(data):
        if campaign.get("campaign_id") == id:
            data.pop(index)
            return Response(status_code=204)
    raise HTTPException(status_code=404, detail="Campaign not found")