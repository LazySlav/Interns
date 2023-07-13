from uuid import UUID
from fastapi import APIRouter, HTTPException
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
  try:
    return await read_entity(ASYNC_SESSIONMAKER, CompanyModel, id=id)
  except Exception as error:
    raise HTTPException(status_code=404) from error

@router.post("/",response_model=CompanySchema)
async def post_Company(payload: CompanySchema):
  try:
    return await create_entity(ASYNC_SESSIONMAKER, CompanyModel, payload)
  except Exception as error:
    raise HTTPException(status_code=500) from error