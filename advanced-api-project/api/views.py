from rest_framework import generics, filters
from django_filters import rest_framework as django_filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# List all books
class BookListView(generics.ListAPIView):
    """
    Retrieve a list of all books with advanced query capabilities:
    - Filtering by title, author, publication_year
    - Searching by title and author name
    - Ordering by title or publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # ✅ Filtering, searching, and ordering belong here
    filter_backends = [django_filters.DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    # Filtering by model fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching (title and author name)
    search_fields = ['title', 'author__name']

    # Ordering options
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering


# Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by ID.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Create a new book
class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
