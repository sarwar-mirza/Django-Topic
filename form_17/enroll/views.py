from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def stu_regi(request):
    fm = StudentRegistration()
    return render(request, 'enroll/registration.html', {'form': fm})
