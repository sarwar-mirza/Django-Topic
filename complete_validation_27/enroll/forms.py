from django import forms

class StudentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()

        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        valpass = self.cleaned_data['password']

        if len(valname)<=4:
            raise forms.ValidationError('Name should be more than or equal 4')
        
        if len(valemail)<=10:
            raise forms.ValidationError("Email should be more than or equal 10")
        
        if len(valpass)<=6:
            raise forms.ValidationError('Password should be more than or equal 6')
        
        
