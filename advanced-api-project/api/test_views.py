# api/test_views.py
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Author, Book
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    def setUp(self):
        # Set up test client and initial data before each test
        self.client = APIClient()
        
        # Create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        
        # Create an author and books for testing
        self.author = Author.objects.create(name='J.K. Rowling')
        self.book1 = Book.objects.create(
            title='Harry Potter', publication_year=1997, author=self.author
        )
        self.book2 = Book.objects.create(
            title='Chamber of Secrets', publication_year=1998, author=self.author
        )

    # Test CRUD Operations
    def test_create_book_authenticated(self):
        # Test POST /api/books/create/ with authentication
        self.client.login(username='testuser', password='testpass123')
        data = {
            'title': 'Prisoner of Azkaban',
            'publication_year': 1999,
            'author': self.author.id
        }
        response = self.client.post(reverse('book-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data['title'], 'Prisoner of Azkaban')

    def test_create_book_unauthenticated(self):
        # Test POST /api/books/create/ without authentication
        data = {
            'title': 'Goblet of Fire',
            'publication_year': 2000,
            'author': self.author.id
        }
        response = self.client.post(reverse('book-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 2)  # No new book created

    def test_list_books(self):
        # Test GET /api/books/ (unauthenticated should work)
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # 2 books in setup

    def test_retrieve_book(self):
        # Test GET /api/books/<pk>/
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Harry Potter')

    def test_update_book_authenticated(self):
        # Test PUT /api/books/update/<pk>/ with authentication
        self.client.login(username='testuser', password='testpass123')
        url = reverse('book-update', args=[self.book1.id])
        data = {
            'title': 'Harry Potter Updated',
            'publication_year': 1997,
            'author': self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Harry Potter Updated')

    def test_update_book_unauthenticated(self):
        # Test PUT /api/books/update/<pk>/ without authentication
        url = reverse('book-update', args=[self.book1.id])
        data = {
            'title': 'Harry Potter Unauthorized',
            'publication_year': 1997,
            'author': self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.book1.refresh_from_db()
        self.assertNotEqual(self.book1.title, 'Harry Potter Unauthorized')

    def test_delete_book_authenticated(self):
        # Test DELETE /api/books/delete/<pk>/ with authentication
        self.client.login(username='testuser', password='testpass123')
        url = reverse('book-delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        # Test DELETE /api/books/delete/<pk>/ without authentication
        url = reverse('book-delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 2)  # Book not deleted

    # Test Filtering, Searching, Ordering
    def test_filter_by_title(self):
        # Test filtering by title (?title=)
        response = self.client.get(reverse('book-list'), {'title': 'Harry Potter'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Harry Potter')

    def test_search_by_author(self):
        # Test searching by author name (?search=)
        response = self.client.get(reverse('book-list'), {'search': 'Rowling'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Both books by Rowling

    def test_order_by_publication_year(self):
        # Test ordering by publication_year (?ordering=)
        response = self.client.get(reverse('book-list'), {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1997)  # Oldest first
        self.assertEqual(response.data[1]['publication_year'], 1998)
