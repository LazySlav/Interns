from django.urls import path
from web.views.mentor import *


mentorpatterns = [
    path('mentors/',post_profile, name='mentor-list'),
    path('mentors/<uuid:id>', get_put_delete_profile, name='mentor-detail')
]