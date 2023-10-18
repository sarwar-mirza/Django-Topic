from django.core import validators
from django import forms
from enroll.models import RegistrationForm


class StudentForm(forms.ModelForm):
    class Meta:
        model = RegistrationForm

        fields = ['name', 'email', 'password']

        labels = {'name':'Full Name'}

        widgets = {'password': forms.PasswordInput(attrs={'placeholder':'Enter your passwrod'})}

