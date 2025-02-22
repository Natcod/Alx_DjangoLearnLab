from django.shortcuts import render
from django.views.generic import DetailView

from .models import Book
from .models import Library

# Function-based view
def list_books(request):
    books = Book.objects.all()

    return render(request, 'list_books.html', {'books': books})
    

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context