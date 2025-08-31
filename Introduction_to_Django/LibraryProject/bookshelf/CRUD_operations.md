# CRUD Operations for the Book Model

## Create
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Output: <Book: 1984 by George Orwell (1949)>
```

## Retrieve
```python
b = Book.objects.first()
b.title, b.author, b.publication_year
# Output: ('1984', 'George Orwell', 1949)
```

## Update
```python
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>
```

## Delete
```python
b = Book.objects.get(title="Nineteen Eighty-Four")
b.delete()
# Output: <QuerySet []>
```

