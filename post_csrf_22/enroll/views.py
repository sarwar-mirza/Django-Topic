from django.shortcuts import render
from enroll.forms import StudentForm
# Create your views here.

def regi_form(request):
    fm = StudentForm()
    return render(request, 'enroll/forms.html', {'form':fm})