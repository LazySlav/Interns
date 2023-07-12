"""
This file is for connecting routers and creating DB engine
"""


from fastapi import FastAPI
import os
from app.models import Base
from sqlalchemy.ext.asyncio import async_sessionmaker,create_async_engine
from fastapi import FastAPI
from fastapi_async_sqlalchemy import SQLAlchemyMiddleware
from app.routers import companies,curators,mentors,students,users
 
app = FastAPI()
app.add_middleware(
    SQLAlchemyMiddleware,
    db_url="postgresql+asyncpg://user:user@192.168.88.200:5432/primary_db",
    engine_args={              # engine arguments example
        "echo": True,          # print all SQL statements
        "pool_pre_ping": True, # feature will normally emit SQL equivalent to “SELECT 1” each time a connection is checked out from the pool
        "pool_size": 5,        # number of connections to keep open at a time
        "max_overflow": 10,    # number of connections to allow to be opened above pool_size
        "connect_args": {
            "prepared_statement_cache_size": 0,  # disable prepared statement cache
            "statement_cache_size": 0,           # disable statement cache
        },
    },
)
app.include_router(companies.router)
app.include_router(curators.router)
app.include_router(mentors.router)
app.include_router(students.router)
app.include_router(users.router)

##### TODO: migrate all of sqlalchemy initial start stuff into separate file #####
DATABASE_URL = os.getenv("DATABASE_URL")
ENGINE = create_async_engine(DATABASE_URL)
with ENGINE.begin() as conn:
    conn.run_sync(Base.metadata.create_all)

# ? the fuck is this
# for AsyncEngine created in function scope, close and
# clean-up pooled connections
# await ENGINE.dispose()
#     
ASYNC_SESSIONMAKER = async_sessionmaker(ENGINE, expire_on_commit=False) # expire_on_commit - don't expire objects after transaction commit

##############################################################################
