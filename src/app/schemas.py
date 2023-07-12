"""
This file is for pydanctic models (schemas) - validation, type-checking and data conversion
"""


from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4
# from email_validator import validate_email
# from pydantic import field_validator
from pydantic import BaseModel, Field, constr, FutureDatetime
from pydantic_extra_types.phone_numbers import PhoneNumber



##### As for models.py, inheritance should work according to https://python.helpful.codes/tutorials/pydantic/How-to-use-Pydantic-with-Inheritance/ #####
class ID(BaseModel):
  id: UUID = Field(default_factory=uuid4)
  
class HumanSchema(ID):
  name: str = Field(..., max_length=50)
  surname: str = Field(..., max_length=50)
  patronymic: str = Field(..., max_length=50)
  mail: str = Field(..., max_length=50)
  phone: PhoneNumber

class CompanySchema(ID):
  name: str = Field(..., min_length=3, max_length=50)
  legal_address: str = Field(..., min_length=3, max_length=100)
  physical_address: str = Field(..., min_length=3, max_length=100)
  phone: PhoneNumber
  mail: str = Field(..., max_length=50)
  description: str = Field(max_length=1000)
  # ? should we check on backend, or frontend is enough
  # @field_validator('mail')
  # def mail_validation(cls, mail):
  #     try:
  #       return validate_email(mail).normalized
  #     except ...

# ? is this the right/safe way to make status options limited
class VacancyStatus(str, Enum):
  not_checked = "not_checked"
  checked = "checked"
  approved = "approved"
  rejected = "rejected"
  completed = "completed"
   

class VacancySchema(ID):
  # ? should there be checks as well or class's are enough
  company_id: UUID
  curator_id: UUID
  workers: list[tuple[int,constr(max_length=100)]] = [()] 
  status: VacancyStatus
  tasks: str = Field(..., max_length=1000) # TODO: rich text/markdown
  start_date: FutureDatetime # ! might cause trouble
  end_date: FutureDatetime
  address: str = Field(...,max_length=250)
  description: str


class UniversitySchema(BaseModel):
  university_name: str = Field(..., max_length=250)


class CuratorSchema(HumanSchema):
  university: UniversitySchema
  recommended: list[tuple[UUID,constr(max_length=50)]] = [()] # ? this probably needs to be changed to contain extra info


class MentorSchema(HumanSchema):
  curator_id: UUID


class StudentSchema(HumanSchema):
  mentor_id: UUID
  profession: str = Field(..., max_length=50)
  resume: str = Field(...,  max_length=1000)


class TaskStatus(Enum):
  not_checked = "not_checked"
  checked = "checked"
  approved = "approved"
  rejected = "rejected"
  completed = "completed"

class TaskSchema(ID):
  mentor_id: UUID
  student_id: UUID
  description: str = Field(..., max_length=1000)
  status: TaskStatus


class ChatSchema(ID):
  company_id: UUID
  student_id: UUID


class MessageSchema(ID):
  chat_id: UUID
  body: str = Field(..., max_length=1000)
  datetime: datetime # ? additional checks needed or what