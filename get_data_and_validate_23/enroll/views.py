from django.shortcuts import render
from enroll.forms import StudentForm
# Create your views here.

def student_regi(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            print('Name: ', fm.cleaned_data['name'])
            print('Email: ', fm.cleaned_data['email'])
            print('password: ', fm.cleaned_data['password'])

    else:
        fm = StudentForm()

    return render(request, 'enroll/regiinfo.html', {'form':fm})
