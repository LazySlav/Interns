from uuid import UUID
from fastapi import APIRouter
from models import CompanyModel
from schemas import CompanySchema
from crud import *
from main import ASYNC_SESSIONMAKER


router = APIRouter(
  prefix="/companies",
  tags=["companies"]
)


@router.get("/{id}",response_model=CompanySchema)
async def get_Company(id : UUID):
  return await read_entity(ASYNC_SESSIONMAKER, CompanyModel, id=id)

@router.post("/",response_model=CompanySchema)
async def create_Company(payload: CompanySchema):
  return await create_entity(ASYNC_SESSIONMAKER, CompanyModel, payload)