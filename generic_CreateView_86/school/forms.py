from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Your Name','class':'my_name'}),
            'email': forms.EmailInput(attrs={'class':'my_email'}),
            'password': forms.PasswordInput(attrs={'class':'my_pass'})
        }