from django.shortcuts import render
from enroll.forms import RegistrationForm
# Create your views here.
def student_regi(request):
    if request.method == 'POST':
        fm = RegistrationForm(request.POST)
        
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']

            print('Name: ', name)
            print('Name: ', email)
            print('Name: ', password)

    else:
        fm = RegistrationForm()
    return render(request, 'enroll/studentinfo.html', {'form':fm})
    
