"""
URL configuration for join_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from join.views import (
    TaskView,
    SingleTaskView,
    LoginView,
    CreateUserView,
    DeleteUserView,
    CategorysView,
    UserListView,
    ContactView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view()),
    path("tasks/", TaskView.as_view()),
    path("tasks/<int:task_id>/", SingleTaskView.as_view()),
    path("categorys/", CategorysView.as_view()),
    path("users/", UserListView.as_view()),
    path("create_user/", CreateUserView.as_view()),
    path("delete_user/", DeleteUserView.as_view()),
    path("contacts/", ContactView.as_view()),
    path("contacts/<int:contact_id>/", ContactView.as_view()),
    path(
        "password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
]
