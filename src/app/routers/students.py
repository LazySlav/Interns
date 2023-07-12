from fastapi import APIRouter
from main import ASYNC_SESSIONMAKER
from models import *
from schemas import *
from crud import *
from uuid import UUID


router = APIRouter(
    prefix="/students",
    tags=['student']
)

@router.get("/", response_model=List[StudentSchema])
async def get_students():
   return await read_all_entities(ASYNC_SESSIONMAKER, StudentModel)

@router.get("/{id}", response_model=StudentSchema)
async def get_student(id : UUID):
    return await read_entity(ASYNC_SESSIONMAKER, StudentModel, id=id)


@router.post("/create", response_model=StudentSchema)
async def create_student(payload:StudentSchema):
    return await create_entity(ASYNC_SESSIONMAKER, StudentModel, payload)


@router.put("/{id}/edit", response_model=StudentSchema)
async def update_student(payload:StudentSchema):
    return await update_entity(ASYNC_SESSIONMAKER, StudentModel, payload)
