import types
from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import UUID
from django.contrib.postgres.fields import ArrayField
import types

class ID():
    id = models.UUIDField(primary_key=True)


class UserModel(AbstractUser):
    ROLE = [
        ("Company", "Company"),
        ("Student", "Student"),
        ("Curator", "Curator"),
        ("Mentor", "Mentor"),
    ]
    login = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=10, choices=ROLE)


class HumanModel():
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)


class University(models.Model):
    university_name = models.CharField(max_length=100, primary_key=True)


# class Recommend(types.TypeDecorator):
#     impl = types.
#     def process_bind_param(self, value, dialect):
#         if value is not None:
#             student_id, comment = value
#             return f"{student_id},{comment}"

#     def process_result_value(self, value, dialect):
#         if value is not None:
#             student_id, comment = value.split(",")
#             return (student_id, comment)


class CuratorModel(models.Model, ID, HumanModel):
    login = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    password = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    recommended = models.CharField(Recommend())

    university_relationship = models.OneToOneField("University", backref='curators', lazy=True)
    login_relationship = models.relationship(
        UserModel, backref='users', lazy=True, foreign_keys='UserModel.login')
    password_relationship = models.relationship(
        UserModel, backref="users", lazy=True, foreign_keys='UserModel.password')


class CompanyModel(models.Model, ID):
    login = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    password = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    legal_address = models.CharField(max_length=200)
    physical_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    mail = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    login_relationship = models.relationship(
        UserModel, backref='users', lazy=True, foreign_keys='UserModel.login')
    password_relationship = models.relationship(
        UserModel, backref="users", lazy=True, foreign_keys='UserModel.password')


class MentorModel(models.Model, ID, HumanModel):
    login = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    password = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    curator_id = models.ForeignKey(CuratorModel, on_delete=models.CASCADE)

    curator = models.relationship(
        CuratorModel, backref='mentors', lazy=True)
    login_relationship = models.relationship(
        UserModel, backref='users', lazy=True, foreign_keys='UserModel.login')
    password_relationship = models.relationship(
        UserModel, backref="users", lazy=True, foreign_keys='UserModel.password')


class StudentModel(models.Model, ID, HumanModel):
    login = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    password = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    mentor_id = models.ForeignKey(MentorModel, on_delete=models.CASCADE)
    profession = models.CharField(max_length=30)
    resume = models.CharField(max_length=1000)
    active_vacancy = models.ForeignKey(
        "VacancyModel", on_delete=models.CASCADE, null=True)
    vacancy_history = models.ArrayField(
        models.UUIDField(), null=True)
    __table_args__ = (
        models.Index('student_short', 'name', 'surname', 'patronymic',
                     'profession', 'mentor_id', unique=True),
    )


# class Workers(types.TypeDecorator):
#     impl = types.String

#     def process_bind_param(self, value, dialect):
#         if value is not None:
#             profession, count = value
#             return f"{profession},{count}"

#     def process_result_value(self, value, dialect):
#         if value is not None:
#             profession, count = value.split(",")
#             return (profession, int(count))
        

class VacancyModel(models.Model, ID):
    company_id = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    curator_id = models.UUIDField()
    workers = models.ArrayField(Workers())
    status = models.CharField(max_length=100)
    tasks = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    address = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    company = models.relationship(
        CompanyModel, backref='vacancies', lazy=True)


class TaskModel(models.Model, ID):
    TASKSTATUS = [
        ("not_checked", "not_checked"),
        ("checked", "checked"),
        ("approved", "approved"),
        ("rejected", "rejected"),
        ("completed", "completed"),
    ]
    mentor_id = models.ForeignKey(MentorModel, on_delete=models.CASCADE)
    student_id = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=20, choices=TASKSTATUS)

    mentor = models.relationship(
        MentorModel, backref='tasks', lazy=True)
    student = models.relationship(
        StudentModel, backref='tasks', lazy=True)


class ChatModel(models.Model, ID):
    company_id = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE)
    student_id = models.ForeignKey(
        StudentModel, on_delete=models.CASCADE)

    company = models.relationship(
        CompanyModel, backref='chats', lazy=True)
    student = models.relationship(
        StudentModel, backref='chats', lazy=True)


class MessageModel(models.Model, ID):
    chat_id = models.ForeignKey(ChatModel, on_delete=models.CASCADE)
    body = models.CharField(max_length=1000)
    date_time = models.DateTimeField(auto_now_add=True)

    chat = models.relationship(
        ChatModel, backref='messages', lazy=True)