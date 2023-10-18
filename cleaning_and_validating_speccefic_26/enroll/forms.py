from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_name(self):                         #syntax- def clean_FieldName(self):
        valid = self.cleaned_data['name']

        if len(valid) <= 4:
            raise forms.ValidationError('Enter more than or equal 4 character in this Field')
        return valid