from sqlalchemy import ForeignKey, Table, Index, Column, \
                       DateTime, TIMESTAMP
from sqlalchemy.dialects.postgresql import TEXT, DATE, \
                       BOOLEAN, ARRAY, VARCHAR, UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from uuid import UUID, uuid4
from dataclasses import dataclass
from sqlalchemy import types

Base = declarative_base()


class Human(Base):
  name = Column(VARCHAR(100))
  surname = Column(VARCHAR(100))
  patronymic = Column(VARCHAR(100))
  mail = Column(VARCHAR(100))
  phone = Column(VARCHAR(11))



class CompanyModel(Base):
    __tablename__ = 'companies'
    company_id = Column(UUID , primary_key=True, index=True)
    name = Column(VARCHAR(100), nullable=False)
    legal_address = Column(VARCHAR(200), nullable=False)
    physical_address = Column(VARCHAR(200), nullable=False)
    phone = Column(VARCHAR(20), nullable=False)
    mail = Column(VARCHAR(100), nullable=False)
    description = Column(VARCHAR(500), nullable=False)


class Workers(types.TypeDecorator):
    impl = types.String

    def process_bind_param(self, value, dialect):
        if value is not None:
            profession, count = value
            return f"{profession},{count}"

    def process_result_value(self, value, dialect):
        if value is not None:
            profession, count = value.split(",")
            return (profession, int(count))

class Vacancy(Base):
    __tablename__ = 'vacancies'
    vacancy_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    company_id = Column(UUID(as_uuid=True), nullable=False)
    curator_id = Column(UUID(as_uuid=True), nullable=False)
    workers = Column(ARRAY(Workers()), nullable=False)
    status = Column(VARCHAR(100), nullable=False)
    tasks = Column(VARCHAR(250), nullable=False)
    start_date = Column(DATE, nullable=False)
    end_date = Column(DATE, nullable=False)
    address = Column(VARCHAR(250), nullable=False)
    description = Column(VARCHAR(250))

    company = relationship('Company', backref='vacancies', lazy=True)


class University(Base):
   university_name = Column(VARCHAR())  


class Recommend(types.TypeDecorator):
    impl = types.String

    def process_bind_param(self, value, dialect):
        if value is not None:
            student_id, comment = value
            return f"{student_id},{comment}"

    def process_result_value(self, value, dialect):
        if value is not None:
            student_id, comment = value.split(",")
            return (student_id, comment)

class Curator(Human):
  curator_id = Column(UUID, primary_key=True)
  university = Column(VARCHAR(100), nullable=False) # note: 'type university'
  recommended = Column(Recommend())



class Mentor(Human):
    __tablename__ = 'mentors'
    mentor_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    curator_id = Column(UUID(as_uuid=True), ForeignKey('curators.curator_id'), nullable=False)

    curator = relationship('Curator', backref='mentors', lazy=True)


class Student(Human):
    __tablename__ = 'tudents'
    student_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    mentor_id = Column(UUID(as_uuid=True), ForeignKey('mentors.mentor_id'), nullable=False)
    profession = Column(VARCHAR(30), nullable=False)
    resume = Column(VARCHAR(1000))

    __table_args__ = (
        Index('student_short', 'name', 'urname', 'patronymic', 'profession', 'entor_id', unique=True),
    )

    mentor = relationship('Mentor', backref='students', lazy=True)


class TaskStatus(Enum):
  ...

class Task(Base):
    __tablename__ = 'tasks'
    task_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    mentor_id = Column(UUID(as_uuid=True), ForeignKey('mentors.mentor_id'), nullable=False)
    student_id = Column(UUID(as_uuid=True), ForeignKey('students.student_id'), nullable=False)
    description = Column(VARCHAR(1000), nullable=False)
    status = Column(TaskStatus(), nullable=False)

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