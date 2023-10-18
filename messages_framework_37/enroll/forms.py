from django.core import validators
from django import forms
from enroll.models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Enter Your Name'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter Your Email'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Enter Your Password'})
        }