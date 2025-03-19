# blog/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", views.custom_logout, name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

    # CRUD URLs
    path("", views.PostListView.as_view(), name="post_list"),  # Root URL shows post list
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/new/", views.PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
]