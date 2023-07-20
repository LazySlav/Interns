import random
from django.db import models
from django.contrib.auth.models import AbstractUser
# # * In case of POSTGRES - use this
# from django.contrib.postgres.fields import ArrayField
# from django.contrib.postgres.operations import HStoreExtension
# from django.contrib.postgres.fields import HStoreField
# HStoreExtension()
# class WorkersField(ArrayField):


class ID(models.Model):
    id = models.IntegerField(
        primary_key=True, default=random.randint(100_000, 2_147_483_646), editable=False)

    class Meta:
        abstract = True


# class UserModel(AbstractUser):
#     ROLE = [
#         ("Company", "Company"),
#         ("Student", "Student"),
#         ("Curator", "Curator"),
#         ("Mentor", "Mentor"),
#     ]
#     role = models.CharField(max_length=10, choices=ROLE)


class HumanModel():
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)


class University(models.Model):
    university_name = models.CharField(max_length=100, primary_key=True)


class Recommend(models.Model):
    curator_id = models.IntegerField(primary_key=True)
    student_id = models.IntegerField()
    comment = models.CharField(max_length=255, blank=True)

    # def __str__(self):
    #     return f"{self.student_id}: {self.comment}"

    class Meta:
        db_table = "recommend"


class CuratorModel(ID, HumanModel):
    # login = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    # password = models.ForeignKey(
    #     UserModel, on_delete=models.CASCADE)
    university = models.ForeignKey(
        University, on_delete=models.CASCADE)
    recommended = models.ForeignKey(
        Recommend, on_delete=models.CASCADE, blank=True)


class CompanyModel(ID):
    # login = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    # password = models.ForeignKey(
    #     UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    legal_address = models.CharField(max_length=200)
    physical_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    mail = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)


class MentorModel(ID, HumanModel):
    # login = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    # password = models.ForeignKey(
    #     UserModel, on_delete=models.CASCADE)
    curator_id = models.ForeignKey(
        CuratorModel, on_delete=models.CASCADE)


class Workers(models.Model):
    vacancy_id = models.IntegerField(primary_key=True)
    profession = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.profession}: {self.amount}"

    class Meta:
        db_table = "workers"


class VacancyModel(ID):
    VACANCYSTATUS = [
        ('not_checked', 'not_checked'),
        ('checked', 'checked'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
        ('completed', 'completed')
    ]
    company_id = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE)
    curator_id = models.IntegerField()
    workers = models.ForeignKey(Workers, on_delete=models.CASCADE, blank=True)
    status = models.CharField(
        max_length=20, choices=VACANCYSTATUS)
    tasks = models.CharField(max_length=250)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=250)
    description = models.CharField(max_length=250)


class StudentModel(ID, HumanModel):
    # login = models.ForeignKey(
    #     UserModel, on_delete=models.CASCADE, db_index=True)
    # password = models.ForeignKey(
    #     UserModel, on_delete=models.CASCADE)
    mentor_id = models.ForeignKey(
        MentorModel, on_delete=models.CASCADE)
    profession = models.CharField(
        max_length=30, db_index=True)
    resume = models.CharField(max_length=1000, blank=True)
    active_vacancy = models.ForeignKey(
        VacancyModel, on_delete=models.CASCADE, blank=True)
    # __table_args__ = (
    #     models.Index('student_short', 'name', 'surname', 'patronymic',
    #                  'profession', 'mentor_id')
    # )


# class TaskModel(ID):
#     TASKSTATUS = [
#         ("not_checked", "not_checked"),
#         ("checked", "checked"),
#         ("approved", "approved"),
#         ("rejected", "rejected"),
#         ("completed", "completed"),
#     ]
#     mentor_id = models.ForeignKey(MentorModel, on_delete=models.CASCADE)
#     student_id = models.FosreignKey(StudentModel, on_delete=models.CASCADE)
#     description = models.CharField(max_length=1000)
#     status = models.CharField(max_length=20, choices=TASKSTATUS)


# class ChatModel(ID):
#     company_id = models.ForeignKey(
#         CompanyModel, on_delete=models.CASCADE)
#     student_id = models.ForeignKey(
#         StudentModel, on_delete=models.CASCADE)


# class MessageModel(ID):
#     chat_id = models.ForeignKey(ChatModel, on_delete=models.CASCADE)
#     body = models.CharField(max_length=1000)
#     date_time = models.DateTimeField(auto_now_add=True)
