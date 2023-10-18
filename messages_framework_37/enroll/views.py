from django.shortcuts import render
from enroll.models import User
from enroll.forms import StudentRegistration
from django.contrib import messages
# Create your views here.

def student_regi(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)

        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']

            reg = User(name = nm, email = em, password = pw)
            reg.save()

            messages.success(request, 'Your account has been Created Successfully!!!')
            messages.info(request, 'Now You Can Login!!!')
            messages.warning(request, 'This is Warning!!!')
            messages.error(request, 'This is Error messages!!!')

            
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/stuinfo.html', {'form':fm})
