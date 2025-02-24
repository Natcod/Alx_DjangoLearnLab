from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

# Helper functions to check user roles
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Admin View
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html', {'role': 'Admin'})

# Librarian View
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html', {'role': 'Librarian'})

# Member View
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html', {'role': 'Member'})