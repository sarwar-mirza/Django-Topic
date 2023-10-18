from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(min_length=4, max_length=10,strip=False, empty_value='mithu', error_messages={'required': 'Enter Your name'})
    roll = forms.IntegerField(min_value=4, max_value=20)
    price = forms.DecimalField(min_value=5, max_value=50, max_digits=4, decimal_places=1)
    rate = forms.FloatField(min_value=10, max_value=15)
    comment = forms.SlugField()
    email = forms.EmailField(min_length=6, max_length=40)
    password = forms.CharField(min_length=5, max_length=40, widget=forms.PasswordInput())
    website = forms.URLField(min_length=5, max_length=50)
    description = forms.CharField(widget=forms.Textarea())
    feedback = forms.CharField(min_length=5, max_length=50, widget=forms.TextInput(attrs={'class': 'session1, session2', 'id':'name'}))
    note = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':50}))
    agree = forms.BooleanField(label_suffix=' ', label='I Agree')
