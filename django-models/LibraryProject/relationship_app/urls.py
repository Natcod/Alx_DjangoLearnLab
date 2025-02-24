from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Function-based view for listing all books
    path('books/', views.list_books, name='list_books'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
    path('books/add/', add_book, name='add_book'),


    # Class-based view for displaying library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
   # Use Django's built-in LoginView
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    
    # Use Django's built-in LogoutView
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    # Keep the custom registration view
    path('register/', views.register_view, name='register'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]