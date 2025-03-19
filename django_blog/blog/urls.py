# blog/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", views.custom_logout, name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
]