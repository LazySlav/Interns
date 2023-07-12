from pydantic import BaseModel as BaseSchema
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select, update, delete
from typing import List
from fastapi import APIRouter
router = APIRouter()


async def read_all_entities(async_session: async_sessionmaker[AsyncSession], model_type):
    async with async_session() as session:
        async with session.begin():
            statement = select(model_type).all()
            return await session.scalars(statement).all()

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

async def create_entity(async_session: async_sessionmaker[AsyncSession], model_type, model: BaseSchema):
    async with async_session() as session:
        async with session.begin():
            entity = model_type(**model.model_dump())
            await session.add(entity)
            return entity

async def create_entity_list(async_session: async_sessionmaker[AsyncSession], model_type, model_list: List[BaseSchema]):
    async with async_session() as session:
        async with session.begin():
            entity_list = [model_type(**model.model_dump()) for model in model_list]
            await session.add_all(entity_list)
            return entity_list

async def update_entity(async_session: async_sessionmaker[AsyncSession], model_type, model: BaseSchema):
    async with async_session() as session:
        async with session.begin():
            entity_dict = model.model_dump()
            entity = model_type(**entity_dict)
            query = update(model_type,[entity_dict])
            await session.execute(query)
            return entity

async def delete_entity(async_session: async_sessionmaker[AsyncSession], model_type, model: BaseSchema):
    async with async_session() as session:
        async with session.begin():
            entity_dict = model.model_dump()
            entity = model_type(**entity_dict)
            query = delete(model_type,[entity_dict])
            await session.execute(query)
            return entity