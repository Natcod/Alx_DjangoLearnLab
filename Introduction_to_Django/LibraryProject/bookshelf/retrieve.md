
---

### **c. Update the Title of the Created Book**

#### Command:
```python
# Retrieve the book to update
book_to_update = Book.objects.get(title="1984")

# Update the title
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()

# Print the updated book
print(book_to_update)