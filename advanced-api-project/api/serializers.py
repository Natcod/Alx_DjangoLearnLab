# api/serializers.py
from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer handles serialization of Book model instances.
# It includes all fields and adds custom validation for publication_year.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']  # Serialize all Book fields

    def validate_publication_year(self, value):
        # Ensures the publication year is not in the future
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer handles serialization of Author model instances.
# It includes the author's name and a nested representation of all their books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer for related books

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']  # Serialize name and related books

    # Note: The relationship between Author and Book is handled via the 'books' field.
    # The related_name='books' in the Book model's author field allows us to access
    # all books written by an author dynamically. The BookSerializer is nested here
    # to provide detailed book info within each author's serialized data.