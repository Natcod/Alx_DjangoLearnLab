from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")

# List all books in a library
def query_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")

# Retrieve the librarian for a library
def query_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"The librarian for {library_name} is {librarian.name}.")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")