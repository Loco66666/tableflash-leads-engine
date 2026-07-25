from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class RestaurantCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    address: str | None = None
    city: str | None = Field(default=None, max_length=120)
    postal_code: str | None = Field(default=None, max_length=20)
    phone: str | None = Field(default=None, max_length=32)
    email: str | None = Field(default=None, max_length=320)
    website: str | None = None


class RestaurantRead(RestaurantCreate):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    created_at: datetime
    updated_at: datetime
