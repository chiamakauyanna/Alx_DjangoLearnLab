from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm


# -----------------------------
# View all books
# -----------------------------
@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


# -----------------------------
# Create new book
# -----------------------------
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        year = request.POST.get("publication_year")
        # ORM prevents SQL injection automatically
        Book.objects.create(title=title, author=author, publication_year=year)
        return redirect("list_books")
    return render(request, "bookshelf/book_form.html")


# -----------------------------
# Edit existing book
# -----------------------------
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.publication_year = request.POST.get("publication_year")
        book.save()
        return redirect("list_books")
    return render(request, "bookshelf/book_form.html", {"book": book})


# -----------------------------
# Delete a book
# -----------------------------
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect("list_books")


# -----------------------------
# Example form with CSRF + safe handling
# -----------------------------
def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Access cleaned data (safe from XSS/SQL injection)
            title = form.cleaned_data["title"]
            author = form.cleaned_data["author"]
            year = form.cleaned_data["publication_year"]

            # Example: create book securely
            Book.objects.create(title=title, author=author, publication_year=year)

            return render(request, "bookshelf/form_example.html", {
                "form": ExampleForm(),   # show empty form again
                "success": True
            })
    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form})
