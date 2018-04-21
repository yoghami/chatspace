from django import forms
from index.models import Room


class RoomForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control',
                                                         'placeholder': 'Enter group name'}))
    secretcode = forms.CharField(widget=forms.PasswordInput())
    secretcode.widget.attrs.update({'class': 'form-control', 'placeholder': 'password', 'type': 'password',
                                    'name': 'password'})

    class Meta:
        model = Room
        fields = '__all__'


class JoinForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control',
                                                         'placeholder': 'Enter group name'}))
    secretcode = forms.CharField(widget=forms.PasswordInput())
    secretcode.widget.attrs.update({'class': 'form-control', 'placeholder': 'password', 'type': 'password',
                                    'name': 'password'})