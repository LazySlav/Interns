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

ROUTERS_PATH = "web.routers."

urlpatterns = [
    path('admin/', admin.site.urls),
    path("companies/<id>/", include(ROUTERS_PATH+"company")),
    # path("curators/<id>/", include(ROUTERS_PATH+"curator")),
    # path("mentors/<id>/", include(ROUTERS_PATH+"mentor")),
    # path("students/<id>", include(ROUTERS_PATH+"student")),
]
