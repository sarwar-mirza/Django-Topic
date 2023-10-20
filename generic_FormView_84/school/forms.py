from django import forms

class ContratForm(forms.Form):
    name = forms.CharField(max_length=70)
    email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)