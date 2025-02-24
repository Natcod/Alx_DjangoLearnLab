from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import DetailView
from .models import Book, Library
from django.core.exceptions import PermissionDenied

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library  
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Helper function to check user roles
def check_role(user, role):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role

# Admin View
@login_required
@user_passes_test(lambda user: check_role(user, 'Admin'), login_url='/login/')
def admin_view(request):
    return render(request, 'admin_view.html', {'role': 'Admin'})

# Librarian View
@login_required
@user_passes_test(lambda user: check_role(user, 'Librarian'), login_url='/login/')
def librarian_view(request):
    return render(request, 'librarian_view.html', {'role': 'Librarian'})

# Member View
@login_required
@user_passes_test(lambda user: check_role(user, 'Member'), login_url='/login/')
def member_view(request):
    return render(request, 'member_view.html', {'role': 'Member'})
