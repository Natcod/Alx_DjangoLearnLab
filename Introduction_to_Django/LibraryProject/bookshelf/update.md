from bookshelf.models import Book

# Retrieve the book to update
book_to_update = Book.objects.get(title="1984")

# Update the title
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()

# Print the updated book details, explicitly showing the title
print(f"Updated Title: {book_to_update.title}, Author: {book_to_update.author}, Publication Year: {book_to_update.publication_year}")