import random
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
# # * In case of POSTGRES - use this
# from django.contrib.postgres.fields import ArrayField
# from django.contrib.postgres.operations import HStoreExtension
# from django.contrib.postgres.fields import HStoreField
# HStoreExtension()
# class WorkersField(ArrayField):


# class UserModel(AbstractUser):
#     ROLE = [
#         ("Company", "Company"),
#         ("Student", "Student"),
#         ("Curator", "Curator"),
#         ("Mentor", "Mentor"),
#     ]
#     role = models.CharField(max_length=10, choices=ROLE)


class ID(models.Model):
    id = models.IntegerField(
        primary_key=True, default=random.randint(100_000, 2_147_483_646), editable=False)

    class Meta:
        abstract = True


class Human(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100,blank=True)
    mail = models.EmailField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17)
    class Meta:
        abstract = True

class CompanyModel(ID):
    # login = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    # password = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    legal_address = models.CharField(max_length=200)
    physical_address = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17)
    mail = models.EmailField(max_length=100)
    description = models.CharField(max_length=500, blank=True)


class CuratorModel(ID, Human):
    # login = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    # password = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    university = models.ForeignKey("UniversityTable", on_delete=models.DO_NOTHING)
    recommended = models.ForeignKey("RecommendedTable", on_delete=models.CASCADE, blank=True,null=True)


class MentorModel(ID, Human):
    # login = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    # password = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    curator = models.ForeignKey(CuratorModel, on_delete=models.DO_NOTHING)


class StudentModel(ID, Human):
    # login = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    # password = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    mentor = models.ForeignKey(MentorModel, on_delete=models.DO_NOTHING)
    profession = models.CharField(
        max_length=30)
    resume = models.CharField(max_length=1000, blank=True)
    active_vacancy = models.ForeignKey("VacancyModel", on_delete=models.DO_NOTHING, blank=True)
    # __table_args__ = (
    #     models.Index('student_short', 'name', 'surname', 'patronymic',
    #                  'profession', 'mentor_id')
    # )


class VacancyModel(ID):
    VACANCYSTATUS = [
        ('not_checked', 'not_checked'),
        ('checked', 'checked'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
        ('completed', 'completed')
    ]
    company = models.ForeignKey(CompanyModel, on_delete=models.DO_NOTHING)
    curator = models.IntegerField()
    status = models.CharField(max_length=20, choices=VACANCYSTATUS)
    tasks = models.CharField(max_length=250)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=250)
    description = models.CharField(max_length=250)



# class TaskModel(ID):
#     TASKSTATUS = [
#         ("not_checked", "not_checked"),
#         ("checked", "checked"),
#         ("approved", "approved"),
#         ("rejected", "rejected"),
#         ("completed", "completed"),
#     ]
#     mentor_id = models.ForeignKey(MentorModel, on_delete=models.DO_NOTHING)
#     student_id = models.FosreignKey(StudentModel, on_delete=models.DO_NOTHING)
#     description = models.CharField(max_length=1000)
#     status = models.CharField(max_length=20, choices=TASKSTATUS)


# class ChatModel(ID):
#     company_id = models.ForeignKey(
#         CompanyModel, on_delete=models.DO_NOTHING)
#     student_id = models.ForeignKey(
#         StudentModel, on_delete=models.DO_NOTHING)


# class MessageModel(ID):
#     chat_id = models.ForeignKey(ChatModel, on_delete=models.DO_NOTHING)
#     body = models.CharField(max_length=1000)
#     date_time = models.DateTimeField(auto_now_add=True)

class UniversityTable(models.Model):
    university = models.CharField(max_length=100, primary_key=True)

class WorkersTable(models.Model):
    vacancy = models.ForeignKey("VacancyModel", primary_key=True, on_delete=models.CASCADE)
    profession = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.profession}: {self.amount}"



class RecommendedTable(models.Model):
    curator = models.IntegerField(primary_key=True)
    student = models.IntegerField()
    comment = models.CharField(max_length=255, blank=True)

    # def __str__(self):
    #     return f"{self.student_id}: {self.comment}"
