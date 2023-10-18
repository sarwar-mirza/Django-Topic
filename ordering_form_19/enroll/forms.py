from django import forms

class StudentForm(forms.Form):
    name = forms.CharField()
    fther_name = forms.CharField()
    mother_name = forms.CharField()
    email = forms.EmailField()