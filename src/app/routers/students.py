from fastapi import APIRouter


router = APIRouter(
    prefix="/students",
    tags=['student']
)

@router.get("/")
async def get_students():
    pass

@router.get("/{student_id}")
async def get_student(student_id: str):
    pass

@router.post("/")
async def create_student(student_data: dict):
    pass

@router.put("/{student_id}")
async def update_student(student_id: str, student_data: dict):
    pass
