from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_mentors():
    pass

@router.get("/{mentor_id}")
async def get_mentor(mentor_id: str):
    pass

@router.post("/")
async def create_mentor(mentor_data: dict):

    pass

@router.put("/{mentor_id}")
async def update_mentor(mentor_id: str, mentor_data: dict):

    pass
