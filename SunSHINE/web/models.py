import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


class ID(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=False)
    class Meta:
        abstract = True


class UserModel(AbstractUser):
    ROLE = [
        ("Company", "Company"),
        ("Student", "Student"),
        ("Curator", "Curator"),
        ("Mentor", "Mentor"),
    ]
    role = models.CharField(max_length=10, choices=ROLE, blank=False)


class HumanModel():
    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    patronymic = models.CharField(max_length=100, blank=False)
    mail = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=11, blank=False)


class University(models.Model):
    university_name = models.CharField(max_length=100, primary_key=True, blank=False)


class Recommend(models.Model):
    student_id = models.IntegerField()
    comment = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.student_id}: {self.comment}"

    class Meta:
        db_table = "recommend"

# class MyModel(models.Model):
#     name = models.CharField(max_length=100)
#     recommendations = ArrayField(models.ForeignKey(Recommend, on_delete=models.CASCADE), blank=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         db_table = "mymodel"


class CuratorModel(ID, HumanModel):
    login = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=False)
    password = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=False)
    university = models.ForeignKey(University, on_delete=models.CASCADE, blank=False)
    recommended = ArrayField(models.ForeignKey(Recommend, on_delete=models.CASCADE), blank=True)



class CompanyModel(ID):
    login = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=False)
    password = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=100, blank=False)
    legal_address = models.CharField(max_length=200, blank=False)
    physical_address = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    mail = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=500)


class MentorModel(ID, HumanModel):
    login = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=False)
    password = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=False)
    curator_id = models.ForeignKey(CuratorModel, on_delete=models.CASCADE, blank=False)


class Workers(models.Model):
    profession = models.CharField(max_length=50)
    count = models.IntegerField()

    def __str__(self):
        return f"{self.profession}: {self.count}"

    class Meta:
        db_table = "workers"

# class MyModel(models.Model):
#     name = models.CharField(max_length=100)
#     workers = ArrayField(models.ForeignKey(Workers, on_delete=models.CASCADE), blank=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         db_table = "mymodel"


class VacancyModel(ID):
    VACANCYSTATUS = [
    ('not_checked', 'not_checked'),
    ('checked', 'checked'),
    ('approved', 'approved'),
    ('rejected', 'rejected'),
    ('completed', 'completed')
    ]
    company_id = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, blank=False)
    curator_id = models.UUIDField(blank=False)
    workers = ArrayField(models.ForeignKey(Workers, on_delete=models.CASCADE), blank=True)
    status = models.CharField(max_length=20, choices=VACANCYSTATUS, blank=False)
    tasks = models.CharField(max_length=250, blank=False)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=250, blank=False)
    description = models.CharField(max_length=250, blank=False)


class StudentModel(ID, HumanModel):
    login = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=False, db_index=True)
    password = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=False)
    mentor_id = models.ForeignKey(MentorModel, on_delete=models.CASCADE, blank=False)
    profession = models.CharField(max_length=30, blank=False, db_index=True)
    resume = models.CharField(max_length=1000)
    active_vacancy = models.ForeignKey(VacancyModel, on_delete=models.CASCADE, null=True, blank=False)
    vacancy_history = ArrayField(models.UUIDField(blank=False), null=True)
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
#     mentor_id = models.ForeignKey(MentorModel, on_delete=models.CASCADE, blank=False)
#     student_id = models.ForeignKey(StudentModel, on_delete=models.CASCADE, blank=False)
#     description = models.CharField(max_length=1000, blank=False)
#     status = models.CharField(max_length=20, choices=TASKSTATUS, blank=False)



# class ChatModel(ID):
#     company_id = models.ForeignKey(
#         CompanyModel, on_delete=models.CASCADE, blank=False)
#     student_id = models.ForeignKey(
#         StudentModel, on_delete=models.CASCADE, blank=False)



# class MessageModel(ID):
#     chat_id = models.ForeignKey(ChatModel, on_delete=models.CASCADE, blank=False)
#     body = models.CharField(max_length=1000, blank=False)
#     date_time = models.DateTimeField(auto_now_add=True, blank=False)