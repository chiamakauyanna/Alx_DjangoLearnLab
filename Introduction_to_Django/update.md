### Update the Book Title

```python
from bookshelf.models import Book

b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()

Book.objects.all()
# Output: <QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>]>
