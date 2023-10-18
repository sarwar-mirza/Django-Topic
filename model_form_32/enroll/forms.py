from django.core import validators
from django import forms
from enroll.models import StudentDatabase

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentDatabase
        fields = ['name', 'email', 'password']
        
        labels = {'name':'Enter Name', 'email':'Enter Email', 'password':'Enter password'}

        error_messages = {
            'name':{'required': 'Enter Your Full Name'},
            'email':{'required': 'Enter Your Email'},
            'password':{'required': 'Enter Your Password'}
        }

        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Plz Enter Your Password'}),
            'name':forms.TextInput(attrs={'class':'myclass',
                                          'placeholder':'Plz Enter Your Name'})
        }
