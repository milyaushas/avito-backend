from fastapi import APIRouter, status, HTTPException
from src.contracts import Tender
from typing import List
from src.service import TenderManagerService
import os

try:
    POSTGRES_CONN = os.environ['POSTGRES_CONN']  # URL-строка для подключения к PostgreSQL в формате postgres://{username}:{password}@{host}:{5432}/{dbname}.
except:
    POSTGRES_CONN = "postgresql://postgres@localhost/avito"

tender_manager = TenderManagerService(postgres_url=POSTGRES_CONN)
api_router = APIRouter(prefix="/api")


@api_router.get("/ping", status_code=status.HTTP_200_OK)
async def ping():
    return "ok"


@api_router.get("/tenders", status_code=status.HTTP_200_OK, response_model=List[Tender])
async def tenders():
    return tender_manager.get_tenders()


@api_router.post("/tenders/new", status_code=status.HTTP_201_CREATED)
async def tenders_new(tender):
    new_tender = tender_manager.create_tender(tender)
    if not new_tender:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return new_tender
