import os
import sys
import django

# Get the base directory (2 levels up from this file: relationship_app/query_samples.py → LibraryProject/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Point to your Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

# Setup Django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def run_queries():
    # Query 1: All books by a specific author
    author_name = "J.K. Rowling"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = author.books.all()
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print("-", book.title)
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")

    # Query 2: List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        print(f"\nBooks in {library_name}:")
        for book in library.books.all():
            print("-", book.title)
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")

    # Query 3: Retrieve the librarian for a library
    try:
        librarian = library.librarian
        print(f"\nThe librarian of {library_name} is {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")


if __name__ == "__main__":
    run_queries()
