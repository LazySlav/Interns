from uuid import UUID
from fastapi import APIRouter
from app.models import CompanyModel
from app.schemas import CompanySchema
from app.crud import *
from app.main import ASYNC_SESSIONMAKER


router = APIRouter(
  prefix="/companies",
  tags=["companies"]
)


@router.get("/{id}",response_model=CompanyModel)
async def get_Company(id : UUID):
  return await read_entity(ASYNC_SESSIONMAKER, CompanyModel, id=id)

@router.post("/",response_model=CompanyModel)
async def create_Company(payload: CompanySchema):
  return await create_entity(ASYNC_SESSIONMAKER, CompanyModel, payload)