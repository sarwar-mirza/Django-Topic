from django import forms

class StudentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    re_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()

        valpass = self.cleaned_data['password']
        valrpass = self.cleaned_data['re_password']

        if valpass != valrpass:
            raise forms.ValidationError('Password does not Match')