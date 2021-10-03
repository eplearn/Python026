from django.forms import ModelForm, TextInput
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
            'abstract': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'abstract',
                'id': 'floatingInput'
            }),
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'text',
                'id': 'floatingInput'
            }),
        }
