from django.db import models

class Author(models.Model):
    """
    Represents an author of books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book written by an author.
    Establishes a one-to-many relationship: one Author → many Books.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,                      # Link to Author model
        on_delete=models.CASCADE,   # Deletes books if author is deleted
        related_name='books'         # Reverse access: author.books.all()
    )

    def __str__(self):
        return self.title
