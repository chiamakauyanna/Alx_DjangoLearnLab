# API Endpoints

- **GET /api/books/** → List all books (public) → `200 OK`
- **GET /api/books/<id>/** → Retrieve a book by ID (public) → `200 OK`
- **POST /api/books/create/** → Create a book (authenticated only) → `201 Created` / `403 Forbidden`
- **PUT /api/books/<id>/update/** → Update a book (authenticated only) → `200 OK` / `403 Forbidden`
- **DELETE /api/books/<id>/delete/** → Delete a book (authenticated only) → `204 No Content` / `403 Forbidden`

### Permissions
- **Unauthenticated users** → Read-only access  
- **Authenticated users** → Full CRUD access  

---

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

---

## Running Tests

To run unit tests for the API:

```bash
python manage.py test api
