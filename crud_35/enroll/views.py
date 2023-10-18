from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import StudentRegistration
from enroll.models import User
# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)

        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']

            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()

    stud = User.objects.all()     #this function will show database table 
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

#This function is used Update/Edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)

        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatedata.html', {'form':fm})


# This function is used delete
def delete_data(requist, id):
    if requist.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()

        return HttpResponseRedirect('/')
