from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import  user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Book, Library 
from .models import Library  # Import both Book and Library models
from django.contrib.auth.models import User

# Function-based view to list all books
def list_books(request):
    # Fetch all books from the database
    books = Book.objects.all()
    
    # Render the template with the list of books
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library  # Use the Library model
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context if needed
        return context

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Helper function to check user roles
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