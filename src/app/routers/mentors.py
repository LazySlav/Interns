
from fastapi import APIRouter
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
    return await read_entity(ASYNC_SESSIONMAKER, StudentModel, id=id)



@router.post("/create",response_model=MentorSchema)
async def create_mentor(payload:MentorSchema):
    return await create_entity(ASYNC_SESSIONMAKER, MentorModel, payload)
    

@router.put("/{id}/edit", response_model=MentorSchema)
async def update_mentor(payload:MentorSchema):
    return await update_entity(ASYNC_SESSIONMAKER, MentorModel, payload)


