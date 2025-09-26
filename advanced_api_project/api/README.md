# API Endpoints

- **GET /api/books/** → List all books (public)
- **GET /api/books/<id>/** → Retrieve a book by ID (public)
- **POST /api/books/create/** → Create a book (authenticated only)
- **PUT /api/books/<id>/update/** → Update a book (authenticated only)
- **DELETE /api/books/<id>/delete/** → Delete a book (authenticated only)

Permissions:
- Unauthenticated users → Read-only access
- Authenticated users → Full CRUD access

## Filtering, Searching, and Ordering

### Filtering
- `/api/books/?publication_year=2024`
- `/api/books/?author=1`
- `/api/books/?title=My Book`

### Searching
- `/api/books/?search=Harry`
- `/api/books/?search=Rowling`

### Ordering
- `/api/books/?ordering=title`
- `/api/books/?ordering=-publication_year`
