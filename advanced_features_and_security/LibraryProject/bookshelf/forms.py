from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title.strip()  # Sanitize by stripping whitespace

class ExampleForm(forms.Form):
    example_input = forms.CharField(max_length=100, required=True)

    def clean_example_input(self):
        example_input = self.cleaned_data['example_input']
        if len(example_input) < 2:
            raise forms.ValidationError("Input must be at least 2 characters long.")
        return example_input.strip()  # Sanitize by stripping whitespace
