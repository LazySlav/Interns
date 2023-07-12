
from uuid import UUID
from fastapi import APIRouter
from app.models import *
from app.schemas import *
from app.crud import *
from app.main import ASYNC_SESSIONMAKER


router = APIRouter(
   prefix="/curator",
   tags=['curator']
)

@router.get("/",response_model=CuratorModel)
async def get_curator(id : UUID):
    return await read_entity(ASYNC_SESSIONMAKER, CuratorModel, id=id)

@router.put("/edit", response_model=CuratorModel)
async def update_mentor(payload:CuratorSchema):
    return await update_entity(ASYNC_SESSIONMAKER, CuratorModel, payload)