from uuid import UUID
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select
from app.models import CompanyModel
from typing import List
from fastapi import APIRouter, HTTPException, Path
from app.schemas import CompanySchema
router = APIRouter()


# def __get_model_attrs(obj : DeclarativeBase):
#     return {i:k for i,k in vars(obj).items() if i[:2]!="__" and i[0]!="_"}

# # * Test
# @router.get("/{id}",status_code=201)
# async def read_entity(async_session: async_sessionmaker[AsyncSession], id: UUID, model: DeclarativeBase):
#     async with async_session() as session:
#         async with session.begin():
#             query = select(__get_model_name(model)).where(__get_model_attrs(model)["id"] == id)
#             return await session.execute(query)

# async def create_entity(async_session: async_sessionmaker[AsyncSession], model: DeclarativeBase):
#     async with async_session() as session:
#         async with session.begin():
#             fake_hashed_password = user.password + "notreallyhashed"
#             db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#             await session.add(db_user)

@router.get("/{id}",status_code=201, response_model=CompanySchema)
async def read_company(async_session: async_sessionmaker[AsyncSession], id: UUID):
    async with async_session() as session:
        async with session.begin():
            query = select(CompanyModel).where(CompanyModel.id == id)
            return await session.execute(query)

@router.post("/",status_code=201,response_model=)
async def create_company(async_session: async_sessionmaker[AsyncSession], id: UUID):
    async with async_session() as session:
        async with session.begin():
            fake_hashed_password = user.password + "notreallyhashed"
            db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
            await session.add(db_user)


async def get_items(session: AsyncSession, skip: int = 0, limit: int = 100):
    return await session.query(models.Item).offset(skip).limit(limit).all()


async def create_user_item(session: AsyncSession, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return await db_item