# Advanced API Project - Views Documentation

## Overview
The project uses DRF generic views for `Book` CRUD, enhanced with filtering, searching, ordering, and tested via unit tests in `api/test_views.py`.

## Testing Strategy
- **Framework**: Uses Django’s test framework with DRF’s `APITestCase` and `APIClient`.
- **Scope**: Tests CRUD operations, filtering/searching/ordering, and permissions for `Book` endpoints.
- **Setup**: Creates a test user, author, and books in `setUp` for each test.

## Test Cases
### CRUD Operations
- **`test_create_book_authenticated`**: POST /api/books/create/ (authenticated, 201 Created).
- **`test_create_book_unauthenticated`**: POST /api/books/create/ (unauthenticated, 401 Unauthorized).
- **`test_list_books`**: GET /api/books/ (200 OK, lists all books).
- **`test_retrieve_book`**: GET /api/books/<pk>/ (200 OK, single book).
- **`test_update_book_authenticated`**: PUT /api/books/update/<pk>/ (authenticated, 200 OK).
- **`test_update_book_unauthenticated`**: PUT /api/books/update/<pk>/ (unauthenticated, 401 Unauthorized).
- **`test_delete_book_authenticated`**: DELETE /api/books/delete/<pk>/ (authenticated, 204 No Content).
- **`test_delete_book_unauthenticated`**: DELETE /api/books/delete/<pk>/ (unauthenticated, 401 Unauthorized).

### Filtering, Searching, Ordering
- **`test_filter_by_title`**: GET /api/books/?title=Harry%20Potter (filters correctly).
- **`test_search_by_author`**: GET /api/books/?search=Rowling (searches title/author).
- **`test_order_by_publication_year`**: GET /api/books/?ordering=publication_year (sorts by year).

## Running Tests
- **Command**: `python manage.py test api`
- **Output**: Expect “Ran 11 tests in X.XXXs OK” if all pass.
- **Interpretation**:
  - “OK”: All tests passed—API works as expected.
  - Failures: Check error messages (e.g., “expected 201, got 400”) and fix views/permissions.

## Other Views
- See previous sections for endpoint details.
