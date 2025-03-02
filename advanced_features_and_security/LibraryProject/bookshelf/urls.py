from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'bookshelf'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='bookshelf/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='bookshelf/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('example/', views.example_form_view, name='example_form'),
]
