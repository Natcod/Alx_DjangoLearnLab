from rest_framework import generics.ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets.ModelViewSet
from rest_framework import permissions.IsAuthenticated

class BookList(ListAPIView):
    """View to list all books - requires authentication via token."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

class BookViewSet(ModelViewSet):
    """ViewSet for CRUD operations on books - requires authentication via token."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restricts all CRUD actions to authenticated users
