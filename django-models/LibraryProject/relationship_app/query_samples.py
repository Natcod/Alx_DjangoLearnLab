from relationship_app.models import Library

# List all books in a library
def query_books_in_library(library_name):
    try:
        # Step 1: Retrieve the Library object using Library.objects.get()
        library = Library.objects.get(name=library_name)

        # Step 2: Use books.all() to retrieve all books in the library
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