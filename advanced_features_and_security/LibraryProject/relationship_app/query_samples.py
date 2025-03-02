from django.core.management import setup_environ
import sys
import os

# Add project directory to Python path and set up Django environment
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from django_models import settings
setup_environ(settings)

from relationship_app.models import Author, Book, Library, Librarian

# Populate some sample data (run this once, e.g., in a shell)
def populate_data():
    author = Author.objects.create(name="J.K. Rowling")
    book1 = Book.objects.create(title="Harry Potter 1", author=author)
    book2 = Book.objects.create(title="Harry Potter 2", author=author)
    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2)
    Librarian.objects.create(name="John Doe", library=library)

# Uncomment to populate data (run once)
# populate_data()

# Query 1: All books by a specific author
def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books:
        print(f"- {book.title}")

# Query 2: List all books in a library
def query_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library_name}:")
    for book in books:
        print(f"- {book.title}")

# Query 3: Retrieve the librarian for a library
def query_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library_name}: {librarian.name}")

# Example usage
if __name__ == "__main__":
    query_books_by_author("J.K. Rowling")
    query_books_in_library("Central Library")
    query_librarian_for_library("Central Library")