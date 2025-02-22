from relationship_app.models import Author, Book

# Query all books by a specific author
def query_books_by_author(author_name):
    try:
        # Step 1: Retrieve the Author object using Author.objects.get()
        author = Author.objects.get(name=author_name)

        # Step 2: Use objects.filter() to retrieve books written by the author
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