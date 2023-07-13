
from uuid import UUID
from fastapi import APIRouter, HTTPException
from models import *
from schemas import *
from crud import *
from main import ASYNC_SESSIONMAKER


router = APIRouter(
   prefix="/curator",
   tags=['curator']
)

@router.get("/",response_model=CuratorSchema)
async def get_curator(id : UUID):
    try:
        return await read_entity(ASYNC_SESSIONMAKER, CuratorModel, id=id)
    except Exception as error:
            raise HTTPException(status_code=404) from error

@router.put("/edit", response_model=CuratorSchema)
async def put_mentor(payload:CuratorSchema):
    try:
        return await update_entity(ASYNC_SESSIONMAKER, CuratorModel, payload)
    except Exception as error:
        raise HTTPException(status_code=500) from error