<<<<<<< HEAD
from relationship_app.models import Author, Book, Library, Librarian
=======
from relationship_app.models import Library
>>>>>>> d9d335e5394d0417d5bec848cd8044c4d0ffb8ee

# List all books in a library
def query_books_in_library(library_name):
    try:
<<<<<<< HEAD
        # Retrieve the Author object
        author = Author.objects.get(name=author_name)

        # Filter books written by the author
        books = Book.objects.filter(author=author)
=======
        # Step 1: Retrieve the Library object using Library.objects.get()
        library = Library.objects.get(name=library_name)

        # Step 2: Use books.all() to retrieve all books in the library
        books = library.books.all()
>>>>>>> d9d335e5394d0417d5bec848cd8044c4d0ffb8ee

        if books.exists():
            print(f"Books in {library_name}:")
            for book in books:
                print(f"- {book.title}")
        else:
            print(f"No books found in library '{library_name}'.")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# List all books in a library
def query_books_in_library(library_name):
    try:
        # Retrieve the Library object
        library = Library.objects.get(name=library_name)

        # Retrieve all books in the library
        books = library.books.all()

        if books.exists():
            print(f"Books in {library_name}:")
            for book in books:
                print(f"- {book.title}")
        else:
            print(f"No books found in library '{library_name}'.")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Retrieve the librarian for a library
def query_librarian_for_library(library_name):
    try:
        # Retrieve the Library object
        library = Library.objects.get(name=library_name)

        # Access the librarian via the OneToOneField
        librarian = library.librarian
        print(f"The librarian for {library_name} is {librarian.name}.")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")
    except Exception as e:
        print(f"An error occurred: {e}")