from django.core import validators
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

#signup form
class SignupForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm password (again)', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        labels = {'email':'Email'}

# change profile update
class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login', 'is_active', 'is_staff']
        labels = {'email':'Email'}