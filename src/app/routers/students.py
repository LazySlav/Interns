from fastapi import APIRouter, HTTPException
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
    try:    
        return await read_all_entities(ASYNC_SESSIONMAKER, StudentModel)
    except Exception as error:
        raise HTTPException(status_code=404, detail=f"ID not found: {error}")

@router.get("/{id}", response_model=StudentSchema)
async def get_student(id : UUID):
    try:
        return await read_entity(ASYNC_SESSIONMAKER, StudentModel, id=id)
    except Exception as error:
        raise HTTPException(status_code=404, detail=f"ID not found: {error}")


@router.post("/create", response_model=StudentSchema)
async def create_student(payload:StudentSchema):
    try:
        return await create_entity(ASYNC_SESSIONMAKER, StudentModel, payload)
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"impossible: {error}")


@router.put("/{id}/edit", response_model=StudentSchema)
async def update_student(payload:StudentSchema):
    try:
        return await update_entity(ASYNC_SESSIONMAKER, StudentModel, payload)
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"impossible: {error}")
