from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=70)
    course = forms.CharField(max_length=70)