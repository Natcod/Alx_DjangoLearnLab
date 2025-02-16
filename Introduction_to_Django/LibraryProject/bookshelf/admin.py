from django.contrib import admin
from .models import Book  # Import the Book model

# Define a custom admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters for publication_year and author
    list_filter = ('publication_year', 'author')

    # Enable search functionality for title and author fields
    search_fields = ['title', 'author']

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)