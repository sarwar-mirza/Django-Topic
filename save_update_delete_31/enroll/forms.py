from django.core import validators
from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(error_messages={'required': 'Enter Your Name'})
    email = forms.EmailField(error_messages={'required': 'Enter Your Email'})
    password = forms.CharField(widget=forms.PasswordInput(), error_messages={'required':'Enter Your Password'})
    re_password = forms.CharField(widget=forms.PasswordInput(), error_messages={'required':'Enter Your Re Password'})


    def clean(self):
        cleaned_data = super().clean()

        valpass = self.cleaned_data['password']
        valrpass = self.cleaned_data['re_password']

        if valpass != valrpass:
            raise forms.ValidationError('Password does not match')