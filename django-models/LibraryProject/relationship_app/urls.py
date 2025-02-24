from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    # Function-based view for listing all books
    path('books/', views.list_books, name='list_books'),

    # Class-based view for displaying library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]