from django.urls import include, path
from web.views.company import *

companypatterns = [
    path("", post_profile),
    path("<uuid:id>", get_put_delete_profile),
    # path("vacancies/<id>",vacancy),
    # path("chats/<id>",chat),
]
