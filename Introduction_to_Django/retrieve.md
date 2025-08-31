### Retrieve the Book

```python
from bookshelf.models import Book

b = Book.objects.first()
b.title, b.author, b.publication_year
# Output: ('1984', 'George Orwell', 1949)
