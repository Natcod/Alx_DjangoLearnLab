# api/models.py
from django.db import models

# Author model represents a person who writes books.
# It has a simple structure with just a name field.
class Author(models.Model):
    name = models.CharField(max_length=200)  # Stores the author's full name

    def __str__(self):
        return self.name  # Human-readable representation for admin and debugging

# Book model represents a published book written by an author.
# It links to Author via a foreign key to establish a one-to-many relationship:
# one author can write many books.
class Book(models.Model):
    title = models.CharField(max_length=200)  # Stores the book's title
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # Links to Author model

    def __str__(self):
        return self.title  # Human-readable representation for admin and debugging