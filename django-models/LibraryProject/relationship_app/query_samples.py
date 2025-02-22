from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def query_books_by_author(author_name):
    try:
        # Retrieve the Author object
        author = Author.objects.get(name=author_name)

        # Filter books written by the author
        books = Book.objects.filter(author=author)

        if books.exists():
            print(f"Books by {author_name}:")
            for book in books:
                print(f"- {book.title}")
        else:
            print(f"No books found for author '{author_name}'.")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")
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

        # Retrieve the librarian using Librarian.objects.get()
        librarian = Librarian.objects.get(library=library)

        print(f"The librarian for {library_name} is {librarian.name}.")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")
    except Exception as e:
        print(f"An error occurred: {e}")