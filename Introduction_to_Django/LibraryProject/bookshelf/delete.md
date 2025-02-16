
---

## **5. Save All Commands and Outputs in `CRUD_operations.md`**

Combine all the commands and outputs into a single Markdown file named `CRUD_operations.md`:

```markdown
# CRUD Operations Documentation

## Create
```python
from bookshelf.models import Book

new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(new_book)