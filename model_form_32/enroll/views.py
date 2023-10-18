from django.shortcuts import render
from enroll.forms import RegistrationForm
from enroll.models import StudentDatabase
# Create your views here.

def student_regi(request):
    if request.method == 'POST':
        fm = RegistrationForm(request.POST)

        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pas = fm.cleaned_data['password']

            reg = StudentDatabase(name = nm, email = em, password = pas)
            reg.save()
    else:
        fm = RegistrationForm()
    return render(request, 'enroll/stuinfo.html', {'form':fm})


