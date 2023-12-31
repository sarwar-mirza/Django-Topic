from django.core import validators
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from blog.models import Post

#signup Form
class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        labels = {'first_name':'First Name',
                  'last_name':'Last Name',
                  'email':'Email'
                  }
        
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                   'first_name':forms.TextInput(attrs={'class':'form-control'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'})
                   }


#Login Form
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))

    password = forms.CharField(label=_("Password"), strip=False, 
                               widget=forms.PasswordInput(attrs={'autocomplete':'currnet-password', 'class':'form-control'}))


#Add Post 
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc']

        labels = {'desc':'Description'}

        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                   'desc':forms.Textarea(attrs={'class':'form-control'})
                   }