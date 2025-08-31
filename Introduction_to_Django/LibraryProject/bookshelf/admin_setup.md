# Django Admin Setup for Book Model

## Objective
Configure the Django Admin interface to manage the **Book** model within the `bookshelf` app.  
Customize the admin interface to display key fields, improve usability with filters, and enable search functionality.

---

## Step 1: Register the Book Model
In `bookshelf/admin.py`:

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
````

---

## Step 2: Customize the Admin Interface

Enhance the admin interface with a custom `BookAdmin` class:

```python
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = ("title", "author", "publication_year")

    # Sidebar filters
    list_filter = ("publication_year", "author")

    # Enable search by title or author
    search_fields = ("title", "author")

# Register Book with the customized admin settings
admin.site.register(Book, BookAdmin)
```

---

## Step 3: Run the Development Server

Start the Django server:

```bash
python manage.py runserver
```

Log in to the admin site at:
👉 `http://127.0.0.1:8000/admin/`

Use the **superuser account** you created with:

```bash
python manage.py createsuperuser
```

---

## Step 4: Result in the Admin Dashboard

After logging in and navigating to **Books** in the admin panel, you will see:

* A table showing `title`, `author`, and `publication_year` for each book.
* Filters on the right sidebar for `publication_year` and `author`.
* A search bar at the top allowing you to search by `title` or `author`.

---

## Final Notes

* The `Book` model is now fully manageable from the Django Admin.
* Customizations improve visibility and make data management more efficient.

---

✅ **Task 2 Complete**: The Book model is registered, customized, and documented for admin use.

```