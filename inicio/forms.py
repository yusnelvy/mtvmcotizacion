"""Docstring"""

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class SignUpForm(ModelForm):
    """Docstring"""
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
            }
        labels = {
            'username': 'Username',
            'password': 'Contraseña',
            'email': 'E-mail del usuario',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            }
