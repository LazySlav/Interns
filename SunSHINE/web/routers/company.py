from django.urls import include, path
from web.views.company import *

urlpatterns = [
    path("profile/", post_profile),
    path("profile/<id>", get_put_delete_profile),
    # path("vacancies/<id>",vacancy),
    # path("chats/<id>",chat),
]
