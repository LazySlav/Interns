
from fastapi import APIRouter
from app.main import ASYNC_SESSIONMAKER
from Interns.src.app.models import *
from app.schemas import *
from crud import *
from uuid import UUID


router = APIRouter(
    prefix="/mentors",
    tags=['mentor']
)


@router.get("/{id}", response_model=MentorModel)
async def get_mentor(id : UUID):
    return await read_entity(ASYNC_SESSIONMAKER, StudentModel, id=id)



@router.post("/create",response_model=MentorModel)
async def create_mentor(payload:MentorSchema):
    return await create_entity(ASYNC_SESSIONMAKER, MentorModel, payload)
    

@router.put("/{id}/edit", response_model=MentorModel)
async def update_mentor(payload:MentorSchema):
    return await update_entity(ASYNC_SESSIONMAKER, MentorModel, payload)


