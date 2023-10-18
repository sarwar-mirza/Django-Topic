from django.shortcuts import render
from .forms import StudentInfo
# Create your views here.
def stu_regi(request):
    fm = StudentInfo(auto_id=True, label_suffix=' ', initial={'name': 'mithu'})
    return render(request, 'enroll/registration.html', {'form':fm})