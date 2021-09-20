from django.forms import ModelForm, TextInput
from .models import Account


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['login', 'email', 'password', 'nickname']
        widgets = {
            'login': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'login',
                'id': 'floatingInput',
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'email',
                'id': 'floatingInput'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'password',
                'id': 'floatingInput'
            }),
            'nickname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'nickname',
                'id': 'floatingInput'
            }),
        }
