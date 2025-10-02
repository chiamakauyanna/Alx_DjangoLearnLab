from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegistrationForm, UserUpdateForm

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally auto-login after registration:
            login(request, user)
            messages.success(request, "Registration successful. Welcome!")
            return redirect("blog:profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegistrationForm()
    return render(request, "blog/register.html", {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("blog:profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})


# List all posts
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"  # create this template
    context_object_name = "posts"
    ordering = ["-created_at"]


# Show details of a single post
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


# Create a new post (only for logged-in users)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update a post (only author can edit)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# Delete a post (only author can delete)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
