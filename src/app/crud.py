from uuid import UUID, uuid4
from pydantic import BaseModel as BaseSchema
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select, insert, update
from app.models import CompanyModel
from typing import List
from fastapi import APIRouter, HTTPException, Path
from app.schemas import CompanySchema
router = APIRouter()

def __get_model_name(obj : object):
    return obj.__class__

# def __get_model_attrs(obj : DeclarativeBase):
#     return {i:k for i,k in vars(obj).items() if i[:2]!="__" and i[0]!="_"}

# ************* Generic Test Methods *******************
# @router.get("/",status_code=201)
async def read_all_entities(async_session: async_sessionmaker[AsyncSession], model_type):
    async with async_session() as session:
        async with session.begin():
            statement = select(model_type).all()
            return await session.scalars(statement).all()

# @router.get("/{id}",status_code=201)
async def read_entity(async_session: async_sessionmaker[AsyncSession], model_type, **kwargs):
    async with async_session() as session:
        async with session.begin():
            statement = select(model_type).filter_by(**kwargs)
            return await session.scalars(statement).all()
        
# async def read_entity_list(async_session: async_sessionmaker[AsyncSession], id_list: List[UUID], model_type):
#     async with async_session() as session:
#         async with session.begin():
#             statement = select(model_type).
#             return await session.scalars(statement).all()

# @router.post("/",status_code=201)
async def create_entity(async_session: async_sessionmaker[AsyncSession], model_type, model: BaseSchema):
    async with async_session() as session:
        async with session.begin():
            entity = model_type(**model.model_dump())
            await session.add(entity)

async def create_entity_list(async_session: async_sessionmaker[AsyncSession], model_type, model_list: List[BaseSchema]):
    async with async_session() as session:
        async with session.begin():
            entity_list = [model_type(**model.model_dump()) for model in model_list]
            await session.add_all(entity_list)

# @router.put("/{id}",status_code=201)
async def update_entity(async_session: async_sessionmaker[AsyncSession], id: UUID, model_type, model: BaseSchema):
    async with async_session() as session:
        async with session.begin():
            query    = model_type(**model.model_dump())
            await session.execute(query)


# @router.get("/{id}",status_code=201, response_model=CompanySchema)
# async def read_company(async_session: async_sessionmaker[AsyncSession], id: UUID):
#     async with async_session() as session:
#         async with session.begin():
#             query = select(CompanyModel).where(CompanyModel.id == id)
#             return await session.execute(query)

# @router.post("/",status_code=201,response_model=CompanySchema)
# async def create_company(async_session: async_sessionmaker[AsyncSession], company: CompanySchema):
#     async with async_session() as session:
#         async with session.begin():
#             db_user = CompanySchema(id=id,)
#             await session.add(db_user)
