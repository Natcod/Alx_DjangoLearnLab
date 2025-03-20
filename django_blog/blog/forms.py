# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

class TagWidget(forms.TextInput):
    """Custom widget for entering tags as a comma-separated string."""
    def __init__(self, attrs=None):
        default_attrs = {"placeholder": "e.g., python, django, tutorial"}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {
            "tags": TagWidget(),  # Use the custom TagWidget
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {"content": forms.Textarea(attrs={"rows": 3})}