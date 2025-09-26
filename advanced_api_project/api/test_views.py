from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user for authenticated requests
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create an author
        self.author = Author.objects.create(name="J.K. Rowling")

        # Create books
        self.book1 = Book.objects.create(
            title="Harry Potter 1", publication_year=1997, author=self.author
        )
        self.book2 = Book.objects.create(
            title="Harry Potter 2", publication_year=1998, author=self.author
        )

        # Endpoints
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book1.id])
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", args=[self.book1.id])
        self.delete_url = reverse("book-delete", args=[self.book1.id])

    # ---------- READ TESTS ----------
    def test_list_books(self):
        """Ensure we can list all books (public endpoint)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book_detail(self):
        """Ensure we can retrieve a single book by ID (public endpoint)."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Harry Potter 1")

    # ---------- CREATE TESTS ----------
    def test_create_book_authenticated(self):
        """Ensure authenticated users can create a book."""
        self.client.login(username="testuser", password="testpass")
        data = {"title": "New Book", "publication_year": 2020, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Ensure unauthenticated users cannot create books."""
        data = {"title": "Blocked Book", "publication_year": 2020, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ---------- UPDATE TESTS ----------
    def test_update_book_authenticated(self):
        """Ensure authenticated users can update a book."""
        self.client.login(username="testuser", password="testpass")
        data = {"title": "Updated Title", "publication_year": 2000, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_update_book_unauthenticated(self):
        """Ensure unauthenticated users cannot update a book."""
        data = {"title": "Hack Attempt", "publication_year": 2001, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ---------- DELETE TESTS ----------
    def test_delete_book_authenticated(self):
        """Ensure authenticated users can delete a book."""
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        """Ensure unauthenticated users cannot delete a book."""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ---------- FILTER, SEARCH, ORDER TESTS ----------
    def test_filter_books_by_publication_year(self):
        """Ensure we can filter books by publication year."""
        response = self.client.get(self.list_url, {"publication_year": 1997})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Harry Potter 1")

    def test_search_books_by_title(self):
        """Ensure we can search books by title."""
        response = self.client.get(self.list_url, {"search": "Harry Potter 2"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Harry Potter 2")

    def test_order_books_by_publication_year_desc(self):
        """Ensure we can order books by publication year descending."""
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
