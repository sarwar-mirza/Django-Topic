from django.shortcuts import render
from enroll.forms import RegistrationForm
# Create your views here.

def student_form(request):
    if request.method == 'POST':
        fm = RegistrationForm(request.POST)

        if fm.is_valid():
            print('Name: ', fm.cleaned_data['name'])
            print('Roll: ', fm.cleaned_data['roll'])
            print('Price: ', fm.cleaned_data['price'])
            print('Rate: ', fm.cleaned_data['rate'])
            print('Commnent: ', fm.cleaned_data['comment'])
            print('Email: ', fm.cleaned_data['email'])
            print('Password: ', fm.cleaned_data['password'])
            print('Website: ', fm.cleaned_data['website'])
            print('Description: ', fm.cleaned_data['description'])
            print('Feedback: ', fm.cleaned_data['feedback'])
            print('Note: ', fm.cleaned_data['note'])
            print('Agree: ', fm.cleaned_data['agree'])

    else:
        fm = RegistrationForm()
    return render(request, 'enroll/regiinfo.html', {'form':fm})

