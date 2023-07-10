from sqlalchemy import ForeignKey, Table, Index, Column, \
                       DateTime, PrimaryKeyConstraint, \
                       UniqueConstraint, ForeignKeyConstraint, TIMESTAMP
from sqlalchemy.dialects.postgresql import TEXT, DATE, \
                       BOOLEAN, ARRAY, VARCHAR, UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from uuid import UUID, uuid4
from dataclasses import dataclass

Base = declarative_base()


# class Human(Base):
#   name = Column(VARCHAR(100))
#   surname = Column(VARCHAR(100))
#   patronymic = Column(VARCHAR(100))
#   mail = Column(VARCHAR(100))


class University(Base):
   university_name = Column(VARCHAR())  


class Company(Base):
    __tablename__ = 'companies'
    company_id = Column(UUID , primary_key=True, index=True)
    name = Column(VARCHAR(100), nullable=False)
    legal_address = Column(VARCHAR(200), nullable=False)
    physical_address = Column(VARCHAR(200), nullable=False)
    phone = Column(VARCHAR(20), nullable=False)
    mail = Column(VARCHAR(100), nullable=False)
    description = Column(VARCHAR(500), nullable=False)
    is_active = Column(BOOLEAN, default=True)

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(DATE)
#     username = Column(VARCHAR(100), nullable=False)
#     email = Column(VARCHAR(100), nullable=False)    
#     password = Column(VARCHAR(200), nullable=False)
    
#     __table_args__ = (
#         PrimaryKeyConstraint('id', name='user_pk'),
#         UniqueConstraint('username'),
#         UniqueConstraint('email'),
#     )


@dataclass
class workers:
    def __init__(self, type: str, count: int):
        self.type = None
        self.count = 0

class Vacancy(Base):
    __tablename__ = 'vacancies'
    vacancy_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    company_id = Column(UUID(as_uuid=True), nullable=False)
    curator_id = Column(UUID(as_uuid=True), nullable=False)
    workers = Column(ARRAY(workers()), nullable=False)
    status = Column(VARCHAR(100), nullable=False)
    description = Column(VARCHAR(250))
    tasks = Column(VARCHAR(250), nullable=False)
    start_date = Column(DATE, nullable=False)
    end_date = Column(DATE, nullable=False)
    address = Column(VARCHAR(250), nullable=False)
    is_active = Column(BOOLEAN, default=True)

    # company = relationship('Company', backref='vacancies', lazy=True)


@dataclass
class recommend:
    def __init__(self, student: UUID, comment: VARCHAR(250)):
        self.student = None
        self.comment = None

class Curator(Base):
  curator_id = Column(UUID, primary_key=True)
  name = Column(VARCHAR(30), nullable=False)
  surname = Column(VARCHAR(30), nullable=False)
  patronymic = Column(VARCHAR(30))
  university = Column(VARCHAR(100), nullable=False) # note: 'type university'
  recommended = Column(recommend())


class Mentor(Base):
    __tablename__ = 'mentors'
    mentor_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(VARCHAR(30), nullable=False)
    surname = Column(VARCHAR(30), nullable=False)
    patronymic = Column(VARCHAR(30))
    mail = Column(VARCHAR(30))
    phone = Column(VARCHAR(30))
    curator_id = Column(UUID(as_uuid=True), ForeignKey('curators.curator_id'), nullable=False)

    curator = relationship('Curator', backref='mentors', lazy=True)


class Student(Base):
    __tablename__ = 'tudents'
    student_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(VARCHAR(30), nullable=False)
    surname = Column(VARCHAR(30), nullable=False)
    patronymic = Column(VARCHAR(30))
    profession = Column(VARCHAR(30), nullable=False)
    mail = Column(VARCHAR(30))
    phone = Column(VARCHAR(30))
    resume = Column(VARCHAR(1000))
    mentor_id = Column(UUID(as_uuid=True), ForeignKey('mentors.mentor_id'), nullable=False)

    __table_args__ = (
        Index('student_short', 'name', 'urname', 'patronymic', 'profession', 'entor_id', unique=True),
    )

    mentor = relationship('Mentor', backref='students', lazy=True)


# class TaskStatus(Enum):
#   # TODO: Task statuses
#   ...

class Task(Base):
    __tablename__ = 'tasks'
    task_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    mentor_id = Column(UUID(as_uuid=True), ForeignKey('mentors.mentor_id'), nullable=False)
    student_id = Column(UUID(as_uuid=True), ForeignKey('students.student_id'), nullable=False)
    description = Column(VARCHAR(1000), nullable=False)
    status = Column(VARCHAR(30), nullable=False)

    mentor = relationship('Mentor', backref='tasks', lazy=True)
    student = relationship('Student', backref='tasks', lazy=True)


class Chat(Base):
    __tablename__ = 'chats'
    chat_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    company_id = Column(UUID(as_uuid=True), ForeignKey('companies.company_id'), nullable=False)
    student_id = Column(UUID(as_uuid=True), ForeignKey('students.student_id'), nullable=False)

    company = relationship('Company', backref='chats', lazy=True)
    student = relationship('Student', backref='chats', lazy=True)


class Messages(Base):
    __tablename__ = 'essages'
    message_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    chat_id = Column(UUID(as_uuid=True), ForeignKey('chats.chat_id'), nullable=False)
    body = Column(VARCHAR(1000), nullable=False)
    date_time = Column(TIMESTAMP(timezone=True), nullable=False)

    chat = relationship('Chat', backref='messages', lazy=True)