# Update Operation

Command:
```python
from bookshelf.models import Book

book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()

# Explicitly print the updated title
print(f"Updated Title: {book_to_update.title}")