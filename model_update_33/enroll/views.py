from django.shortcuts import render
from enroll.forms import StudentForm
from enroll.models import RegistrationForm
# Create your views here.

def student_regi(request):
    if request.method == 'POST':
        pi = RegistrationForm.objects.get(pk=1)
        fm = StudentForm(request.POST, instance=pi)

        if fm.is_valid():
           ''' nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']

            reg = RegistrationForm(name=nm, email=em, password=pw)
            reg.save()'''
           fm.save()
    else:
        fm = StudentForm()
    return render(request, 'enroll/stuinfo.html', {'form':fm})


