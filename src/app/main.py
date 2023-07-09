"""
This file is for connecting routers and connecting to database
"""


from fastapi import FastAPI

from app.tables.companies import engine, metadata
# from app.routers import companies,curators,mentors,students
from app.routers import companies
metadata.create_all(engine)

app = FastAPI()

app.include_router(companies.router, prefix="/companies")
# app.include_router(curators.router, prefix="/curators")
# app.include_router(mentors.router, prefix="/mentors")
# app.include_router(students.router, prefix="/students") 