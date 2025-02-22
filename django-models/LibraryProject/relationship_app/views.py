from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library 
from .models import Library  # Import both Book and Library models

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