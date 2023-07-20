"""
URL configuration for SunSHINE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from web.views import company,curator,mentor,student

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path("companies/<int:id>/", company.get_put_delete_profile),
    path("companies/", company.post_profile),
    path('curators/',curator.post_profile, name='curator-list'),
    path('curators/<int:id>', curator.get_put_delete_profile, name='curator-detail'),
    path('mentors/',mentor.post_profile, name='mentor-list'),
    path('mentors/<int:id>', mentor.get_put_delete_profile, name='mentor-detail'),
    path('students/',student.post_profile, name='student-list'),
    path('students/<int:id>', student.get_put_delete_profile, name='student-detail'),
]
