from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Item

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Tu username',
            'class': 'form-control'
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Tu password',
            'class': 'form-control'
        }
    ))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Tu Username',
            'class': 'form-control'
        }
    ))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Tu Email',
            'class': 'form-control'
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Repite Tu Password',
            'class': 'form-control'
        }
    ))

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'price', 'image']

        widgets = {
            'category': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-select'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-select',
                    'style': 'height: 100px'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'class': 'form-select'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-select'
                }
            ),
            
        }