from django.core import validators
# Define django models and forms by default UserCreationForm and User 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput()) # django lable change
    class Meta:
        model = User    # model User in Django
        fields = ['username', 'first_name', 'last_name', 'email']   # Create extra Fields 

        labels = {'email':'Email'}     # changes labels
