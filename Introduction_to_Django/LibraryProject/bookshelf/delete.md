### Delete the Book

```python
from bookshelf.models import Book

b = Book.objects.get(title="Nineteen Eighty-Four")
b.delete()

Book.objects.all()
# Output: <QuerySet []>
