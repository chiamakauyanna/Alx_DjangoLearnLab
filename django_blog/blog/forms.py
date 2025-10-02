from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

from blog.models import Post

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3, "placeholder": "Write your comment..."}),
        }

    def clean_content(self):
        content = self.cleaned_data.get("content", "").strip()
        if not content:
            raise forms.ValidationError("Comment cannot be empty.")
        # optional: limit length
        if len(content) > 2000:
            raise forms.ValidationError("Comment is too long (max 2000 characters).")
        return content

   