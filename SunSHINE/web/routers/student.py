from django.urls import path
from web.views.student import *


studentpatterns = [
    path('students/',post_profile, name='student-list'),
    path('students/<uuid:id>', get_put_delete_profile, name='student-detail')
]