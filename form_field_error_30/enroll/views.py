from django.shortcuts import render
from enroll.forms import StudentForm
# Create your views here.

def student_regi(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)

        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            rpassword = fm.cleaned_data['re_password']

            print('Name: ', name)
            print('Email: ', email)
            print('Password: ', password)
            print('Re Password: ', rpassword)
    else:
        fm = StudentForm()
    return render(request, 'enroll/stuinfo.html', {'form':fm})    


