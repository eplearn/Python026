from django.forms import ModelForm, TextInput, Textarea
from django.core.exceptions import ValidationError

from .models import NoteModel


class NoteForm(ModelForm):
    class Meta:
        model = NoteModel
        fields = ['author', 'title', 'category', 'abstract', 'text']
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'author',
                'id': 'floatingInput',
            }),
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title',
                'id': 'floatingInput'
            }),
            'category': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'category',
                'id': 'floatingInput'
            }),
            'abstract': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'text',
                'id': 'floatingTextarea1',
                "rows": 5, "cols": 20,
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'text',
                'id': 'floatingTextarea1',
                "rows": 10, "cols": 20,
            }),
        }

    def clean(self):
        cleaned_data = super().clean()

        # extract the author, abstract and text field from the data
        author = self.cleaned_data.get('author')
        abstract = self.cleaned_data.get('abstract')
        text = self.cleaned_data.get('text')

        # conditions
        if len(author) < 5:
            self.add_error('author', 'Minimum 5 characters required')

        if len(abstract) < 10:
            self.add_error('abstract', 'Minimum 10 characters required')

        if len(text) < 25:
            self.add_error('text', 'Note main text should contain a minimum of 25 characters')

        return cleaned_data
