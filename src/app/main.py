"""
This file is for connecting routers and connecting to database
"""


from fastapi import FastAPI
from fastapi_async_sqlalchemy import SQLAlchemyMiddleware

from app.database import engine
# from app.routers import companies,curators,mentors,students
# metadata.create_all(engine)

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
#app.include_router(companies.router, prefix="/companies")
# app.include_router(curators.router, prefix="/curators")
# app.include_router(mentors.router, prefix="/mentors")
# app.include_router(students.router, prefix="/students") 