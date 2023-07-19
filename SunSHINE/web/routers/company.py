from django.urls import path
from web.views.company import *

companytterns = [
    path('',post_profile, name='company-list'),
    path('<uuid:id>', get_put_delete_profile, name='company-detail')
]