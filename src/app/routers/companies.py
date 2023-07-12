from typing import List
from uuid import UUID
from fastapi import APIRouter
from app.models import CompanyModel
from app.schemas import CompanySchema
from app.crud import *
from app.main import ASYNC_SESSIONMAKER
router = APIRouter()

@router.get("/{id}",response_model=CompanySchema)
async def get_company(id : UUID):
  return await read_entity(ASYNC_SESSIONMAKER, CompanyModel, id=id)