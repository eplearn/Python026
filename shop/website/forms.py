from django.forms import ModelForm, TextInput, Textarea
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
                'id': 'floatingTextarea',
                "rows": 5, "cols": 20,
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'text',
                'id': 'floatingTextarea2',
                "rows": 5, "cols": 20,
            }),
        }
