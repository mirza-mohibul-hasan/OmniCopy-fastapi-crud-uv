from fastapi import APIRouter, HTTPException
from sqlmodel import select
from app.models.campaign import Campaign
from app.schemas.campaign import CampaignCreate, CampaignUpdate, ResponseModel
from app.core.database import SessionDep

router = APIRouter(prefix="/campaigns", tags=["campaigns"])


@router.get("/", response_model=ResponseModel[list[Campaign]])
async def read_campaigns(session: SessionDep):
    """Get all campaigns"""
    campaigns = session.exec(select(Campaign)).all()
    return {"data": campaigns}


@router.get("/{id}", response_model=ResponseModel[Campaign])
async def read_campaign(id: int, session: SessionDep):
    """Get a campaign by ID"""
    campaign = session.get(Campaign, id)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return {"data": campaign}


@router.post("/", response_model=ResponseModel[Campaign], status_code=201)
async def create_campaign(campaign: CampaignCreate, session: SessionDep):
    """Create a new campaign"""
    db_campaign = Campaign(**campaign.model_dump())
    session.add(db_campaign)
    session.commit()
    session.refresh(db_campaign)
    return {"data": db_campaign}


@router.put("/{id}", response_model=ResponseModel[Campaign])
async def update_campaign(id: int, campaign_update: CampaignUpdate, session: SessionDep):
    """Update a campaign by ID"""
    db_campaign = session.get(Campaign, id)
    if not db_campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    
    campaign_data = campaign_update.model_dump(exclude_unset=True)
    for key, value in campaign_data.items():
        setattr(db_campaign, key, value)
    
    session.add(db_campaign)
    session.commit()
    session.refresh(db_campaign)
    return {"data": db_campaign}


@router.delete("/{id}", status_code=204)
async def delete_campaign(id: int, session: SessionDep):
    """Delete a campaign by ID"""
    db_campaign = session.get(Campaign, id)
    if not db_campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    
    session.delete(db_campaign)
    session.commit()
    return