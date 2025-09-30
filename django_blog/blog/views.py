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
