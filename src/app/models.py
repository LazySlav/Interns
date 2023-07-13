from sqlalchemy import ForeignKey, Index, Column, TIMESTAMP, Enum
from sqlalchemy.dialects.postgresql import DATE, ARRAY, VARCHAR, UUID
from sqlalchemy.orm import relationship
from sqlalchemy import UUID
from sqlalchemy import types
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs

##### Changes should work properly, see: https://docs.sqlalchemy.org/en/20/orm/inheritance.html#relationships-with-single-table-inheritance #####


class BaseModel(AsyncAttrs, DeclarativeBase):
    pass


class ID():
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)


class UserModel(BaseModel):
    __tablename__ = "users"
    login = Column(VARCHAR(30), primary_key=True, index=True, nullable=False)
    password = Column(VARCHAR(30), index=True, nullable=False)


class HumanModel():
    name = Column(VARCHAR(100))
    surname = Column(VARCHAR(100))
    patronymic = Column(VARCHAR(100))
    mail = Column(VARCHAR(100))
    phone = Column(VARCHAR(11))


class CompanyModel(BaseModel, ID):
    __tablename__ = 'companies'
    login = Column(VARCHAR(30), ForeignKey(UserModel.login, ondelete="CASCADE"), index=True, nullable=False)
    password = Column(VARCHAR(30), ForeignKey(UserModel.password, ondelete='CASCADE'), index=True, nullable=False)
    name = Column(VARCHAR(100), nullable=False)
    legal_address = Column(VARCHAR(200), nullable=False)
    physical_address = Column(VARCHAR(200), nullable=False)
    phone = Column(VARCHAR(20), nullable=False)
    mail = Column(VARCHAR(100), nullable=False)
    description = Column(VARCHAR(500), nullable=False)

    login_relationship = relationship("UserModel", backref='users', lazy=True, foreign_keys='UserModel.login')
    password_relationship = relationship("UserModel", backref="users", lazy=True, foreign_keys='UserModel.password')

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


class VacancyModel(BaseModel, ID):
    __tablename__ = 'vacancies'
    company_id = Column(UUID(as_uuid=True), ForeignKey(
        CompanyModel.id, ondelete='CASCADE'), nullable=False)
    curator_id = Column(UUID(as_uuid=True), nullable=False)
    workers = Column(ARRAY(Workers()), nullable=False)
    status = Column(VARCHAR(100), nullable=False)
    tasks = Column(VARCHAR(250), nullable=False)
    start_date = Column(DATE, nullable=False)
    end_date = Column(DATE, nullable=False)
    address = Column(VARCHAR(250), nullable=False)
    description = Column(VARCHAR(250))

    company = relationship("CompanyModel", backref='vacancies', lazy=True)


class University(BaseModel):
    __tablename__ = "universities"
    university_name = Column(VARCHAR(), primary_key=True)


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


class CuratorModel(BaseModel, ID, HumanModel):
    __tablename__ = "curators"
    login = Column(VARCHAR(30), ForeignKey(UserModel.login, ondelete="CASCADE"), index=True, nullable=False)
    password = Column(VARCHAR(30), ForeignKey(UserModel.password, ondelete='CASCADE'), index=True, nullable=False)
    university = Column(VARCHAR(100), ForeignKey(
        University.university_name, ondelete='CASCADE'), nullable=False)  # note: 'type university'
    recommended = Column(Recommend())

    university_relationship = relationship(
        "University", backref='curators', lazy=True)
    login_relationship = relationship("UserModel", backref='users', lazy=True, foreign_keys='UserModel.login')
    password_relationship = relationship("UserModel", backref="users", lazy=True, foreign_keys='UserModel.password')



class MentorModel(BaseModel, ID, HumanModel):
    __tablename__ = 'mentors'
    login = Column(VARCHAR(30), ForeignKey(UserModel.login, ondelete="CASCADE"), index=True, nullable=False)
    password = Column(VARCHAR(30), ForeignKey(UserModel.password, ondelete='CASCADE'), index=True, nullable=False)
    curator_id = Column(UUID(as_uuid=True), ForeignKey(
        CuratorModel.id, ondelete='CASCADE'), nullable=False)

    curator = relationship("CuratorModel", backref='mentors', lazy=True)
    login_relationship = relationship("UserModel", backref='users', lazy=True, foreign_keys='UserModel.login')
    password_relationship = relationship("UserModel", backref="users", lazy=True, foreign_keys='UserModel.password')



class StudentModel(BaseModel, ID, HumanModel):
    __tablename__ = 'students'
    login = Column(VARCHAR(30), ForeignKey(UserModel.login, ondelete="CASCADE"), index=True, nullable=False)
    password = Column(VARCHAR(30), ForeignKey(UserModel.password, ondelete='CASCADE'), index=True, nullable=False)
    mentor_id = Column(UUID(as_uuid=True), ForeignKey(
        MentorModel.id, ondelete='CASCADE'), nullable=False)
    profession = Column(VARCHAR(30), nullable=False)
    resume = Column(VARCHAR(1000))
    active_vacancy = Column(UUID(as_uuid=True), ForeignKey(
        VacancyModel.id, ondelete="CASCADE"), nullable=True)
    vacancy_history = Column(ARRAY(UUID(as_uuid=True)), nullable=True)
    __table_args__ = (
        Index('student_short', 'name', 'surname', 'patronymic',
              'profession', 'mentor_id', unique=True),
    )

    vacancy = relationship("VacancyModel", backref='vacancies', lazy=True)
    mentor = relationship("MentorModel", backref='students', lazy=True)
    login_relationship = relationship("UserModel", backref='users', lazy=True, foreign_keys='UserModel.login')
    password_relationship = relationship("UserModel", backref="users", lazy=True, foreign_keys='UserModel.password')


class TaskStatus(Enum):
    not_checked = "not_checked"
    checked = "checked"
    approved = "approved"
    rejected = "rejected"
    completed = "completed"


class TaskModel(BaseModel, ID):
    __tablename__ = 'tasks'
    mentor_id = Column(UUID(as_uuid=True), ForeignKey(
        MentorModel.id, ondelete='CASCADE'), nullable=False)
    student_id = Column(UUID(as_uuid=True), ForeignKey(
        StudentModel.id, ondelete='CASCADE'), nullable=False)
    description = Column(VARCHAR(1000), nullable=False)
    status = Column(TaskStatus(), nullable=False)

    mentor = relationship("MentorModel", backref='tasks', lazy=True)
    student = relationship("StudentModel", backref='tasks', lazy=True)


class ChatModel(BaseModel, ID):
    __tablename__ = 'chats'
    company_id = Column(UUID(as_uuid=True), ForeignKey(
        CompanyModel.id, ondelete='CASCADE'), nullable=False)
    student_id = Column(UUID(as_uuid=True), ForeignKey(
        StudentModel.id, ondelete='CASCADE'), nullable=False)

    company = relationship("CompanyModel", backref='chats', lazy=True)
    student = relationship("StudentModel", backref='chats', lazy=True)


class MessageModel(BaseModel, ID):
    __tablename__ = 'messages'
    chat_id = Column(UUID(as_uuid=True), ForeignKey(
        ChatModel.id, ondelete='CASCADE'), nullable=False)
    body = Column(VARCHAR(1000), nullable=False)
    date_time = Column(TIMESTAMP(timezone=True), nullable=False)

    chat = relationship("ChatModel", backref='messages', lazy=True)
