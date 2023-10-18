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

            print('Name: ', name)
            print("Email: ", email)
            print('Password: ', password)
    
    else:
        fm = StudentForm()
    return render(request, 'enroll/sutinfo.html', {'form':fm})

