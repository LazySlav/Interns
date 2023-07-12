
from fastapi import APIRouter, HTTPException
from main import ASYNC_SESSIONMAKER
from models import *
from schemas import *
from crud import *
from uuid import UUID


router = APIRouter(
    prefix="/mentors",
    tags=['mentor']
)


@router.get("/{id}", response_model=MentorSchema)
async def get_mentor(id : UUID):
    try:
        return await read_entity(ASYNC_SESSIONMAKER, StudentModel, id=id)
    except Exception as error:
        raise HTTPException(status_code=404, detail=f"ID not found: {error}")



@router.post("/create",response_model=MentorSchema)
async def create_mentor(payload:MentorSchema):
    try:
        return await create_entity(ASYNC_SESSIONMAKER, MentorModel, payload)
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"impossible: {error}")
    

@router.put("/{id}/edit", response_model=MentorSchema)
async def update_mentor(payload:MentorSchema):
    try:
        return await update_entity(ASYNC_SESSIONMAKER, MentorModel, payload)
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"impossible: {error}")


