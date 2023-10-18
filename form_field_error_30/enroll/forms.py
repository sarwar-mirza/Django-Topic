#from django.core import validators
from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(error_messages={'required': 'Enter Your Name'})
    email = forms.EmailField(min_length=5, max_length=50, error_messages={'required': 'Enter Your Email'})
    password = forms.CharField(widget=forms.PasswordInput(),min_length=5, max_length=50, error_messages={'required':'Enter Your password'})
    re_password = forms.CharField(widget=forms.PasswordInput(),min_length=5, max_length=50, error_messages={'required':'Enter Your Re password'})

    def clean(self):
        cleaned_data = super().clean()

        valpass = self.cleaned_data['password']
        valrpass = self.cleaned_data['re_password']

        if valpass != valrpass:
            raise forms.ValidationError('Password does not mathch')
