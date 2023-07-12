from fastapi import APIRouter
from Interns.src.app.models import Student
from crud import *
from  import 

router = APIRouter(
    prefix="/students",
    tags=['student']
)

@router.get("/", response_model=List[Student])
async def get_students():
   return read_all_entities()

@router.get("/{student_id}", response_model=Student)
async def get_student():
    return read_entity()

@router.post("/")
async def create_student(student_data: dict):
    return create_entity()

@router.put("/{student_id}")
async def update_student(student_id: str, student_data: dict):
    return update_entity()
