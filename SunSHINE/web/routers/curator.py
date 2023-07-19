from django.urls import path
from web.views.curator import *


curatorpatterns = [
    path('curators/',post_profile, name='curator-list'),
    path('curators/<uuid:id>', get_put_delete_profile, name='curator-detail')
]