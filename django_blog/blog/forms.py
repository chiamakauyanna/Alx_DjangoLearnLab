from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Post, Tag   # ✅ added Tag here


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text="Required. Enter a valid email address."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")


class PostForm(forms.ModelForm):
    # a simple comma-separated tags input
    tags = forms.CharField(
        required=False,
        help_text="Comma-separated tags (e.g. django, python, tips).",
        widget=forms.TextInput(attrs={"placeholder": "tag1, tag2, tag3"})
    )

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # populate the tags field with current tag names
            tag_names = ", ".join(t.name for t in self.instance.tags.all())
            self.fields["tags"].initial = tag_names

    def clean_tags(self):
        raw = self.cleaned_data.get("tags", "")
        tag_list = [t.strip() for t in raw.split(",") if t.strip()]
        return tag_list

    def save(self, commit=True):
        tag_list = self.cleaned_data.pop("tags", [])
        post = super().save(commit=commit)
        # if commit=False, tags assignment will still work after post.save()
        post.tags.clear()
        for tag_name in tag_list:
            tag_obj, _ = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag_obj)
        return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Write your comment..."}
            ),
        }

    def clean_content(self):
        content = self.cleaned_data.get("content", "").strip()
        if not content:
            raise forms.ValidationError("Comment cannot be empty.")
        if len(content) > 2000:
            raise forms.ValidationError(
                "Comment is too long (max 2000 characters)."
            )
        return content
