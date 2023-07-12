from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_curators():
    pass

@router.get("/{curator_id}")
async def get_curator(curator_id: str):
    pass

@router.post("/")
async def create_curator(curator_data: dict):
    pass

@router.put("/{curator_id}")
async def update_curator(curator_id: str, curator_data: dict):
    pass
