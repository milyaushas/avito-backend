from pydantic import BaseModel
from enum import Enum


class OrganizationType(Enum):
    IE = 'IE'
    LLC = 'LLC'
    JSC = 'JSC'


class TenderStatus(Enum):
    CREATED = 'CREATED',
    PUBLISHED = 'PUBLISHED',
    CANCELED = 'CANCELED'


class Tender(BaseModel):
    id: int = None
    name: str
    description: str
    serviceType: str
    status: TenderStatus
    organizationId: int
    creatorUsername: str

    class Config:
        orm_model = True
