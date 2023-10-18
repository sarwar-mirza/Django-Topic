from django.shortcuts import render
from enroll.forms import StudentForm
from django.http import HttpResponseRedirect
# Create your views here.

def thankyou(request):
    return render(request, 'enroll/success.html')

def stu_registration(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)

        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            print('Name: ', name)
            print('Email: ', email)
            print('Password: ', password)

            return HttpResponseRedirect('/show/successfully/')      

            #return render(request, 'enroll/success.html', {'name': name})

    else:
        fm = StudentForm()

    return render(request, 'enroll/regiinfo.html', {'form':fm})