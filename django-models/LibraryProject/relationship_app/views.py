from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView

# 🔹 Registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in the new user automatically
            return redirect("list_books")  # redirect to books page
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# 🔹 Login view (using Django's built-in LoginView)
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"
    

# 🔹 Logout view (using Django's built-in LogoutView)
class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"
    
   # Allow GET requests to log out (instead of POST only)
    def get(self, request, *args, **kwargs):
        """Allow GET request to log out user."""
        return super().post(request, *args, **kwargs) 

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})
  
# Class-based view: library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

