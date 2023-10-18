from django.shortcuts import render
from enroll.forms import RegistrationForm
from enroll.models import User

# Create your views here.

def student_regi(requeste):
    if requeste.method == 'POST':
        fm = RegistrationForm(requeste.POST)

        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pas = fm.cleaned_data['password']
            rpas = fm.cleaned_data['re_password']
            rg = User(id=1, name=nm, email = em, password = pas, re_password = rpas)
            rg.save()

            #rg = User(id=1)
            #rg.delete()
    else:
        fm = RegistrationForm()
    return render(requeste, 'enroll/stuinfo.html', {'form':fm})
