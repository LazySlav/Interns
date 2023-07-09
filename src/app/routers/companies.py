from typing import List
from fastapi import APIRouter, HTTPException, Path
from sqlalchemy import Table
from app.schemas import Company

router = APIRouter()

# @router.get("/",response_model=List[Company], status_code=201)
# async def read_notes():
