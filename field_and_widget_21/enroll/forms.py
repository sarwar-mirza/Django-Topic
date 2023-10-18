from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(label='Your Name', label_suffix=' ', required=False, disabled=True, help_text='limit 70 char')


class WidgetForm(forms.Form):
    #PasswordInput(),Textarea(),CheckboxInput(),FileInput()
    feedback = forms.CharField(widget=forms.FileInput())

    # css r maddhome jodi style korthe cai ta hole class,id define kora jabe
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'Class_name', 'id': 'id_name'}))
    