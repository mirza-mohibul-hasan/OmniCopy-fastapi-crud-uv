from datetime import datetime
from typing import Generic, TypeVar
from pydantic import BaseModel


T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    data: T


class CampaignCreate(BaseModel):
    name: str
    due_date: datetime | None = None


class CampaignUpdate(BaseModel):
    name: str | None = None
    due_date: datetime | None = None