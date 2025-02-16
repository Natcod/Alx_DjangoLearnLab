
---

### **d. Delete the Created Book**

#### Command:
```python
# Retrieve the book to delete
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book_to_delete.delete()

# Confirm deletion by retrieving all books
books_after_deletion = Book.objects.all()
print("Books after deletion:", list(books_after_deletion))