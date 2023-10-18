from django.core import validators
from django import forms

def start_with_s(value):
    if value[0] != 'S':
        raise forms.ValidationError('Name should start with S ')

class StudentForm(forms.Form):
    name = forms.CharField(validators=[start_with_s])
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())