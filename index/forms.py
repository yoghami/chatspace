
from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class userRegestration(forms.ModelForm):

    username = forms.CharField(widget =forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'username'}))
    email = forms.EmailField(widget =forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'email'}),required=True)
    password = forms.CharField(widget =forms.PasswordInput())

    password.widget.attrs.update({'class': 'form-control', 'placeholder': 'password', 'type':'password', 'name':'password'})
    class Meta:
        model = User
        fields = ['username', 'password', 'email']








