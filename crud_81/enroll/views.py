from typing import Any
from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import StudentRegistration
from enroll.models import User
from django.views.generic.base import RedirectView, TemplateView
from django.views import View
# Create your views here.
# This Class will add new item and show all items
class UserAddshowView(TemplateView):
    template_name= 'enroll/addandshow.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        stud = User.objects.all()   #this function will show database table
        context = {'form':fm, 'stu':stud}
        return context
    
    def post(self, request):
        fm = StudentRegistration(request.POST)

        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']

            reg = User(name=nm, email=em, password=pw)
            reg.save()
            return HttpResponseRedirect('/')


'''
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
'''
#This function is used Update/Edit
class UserUpdateView(View):
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render(request, 'enroll/updatedata.html', {'form':fm})
    
    def post(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        
        if fm.is_valid():
            fm.save()
            return render(request, 'enroll/updatedata.html', {'form':fm})
'''
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
'''

# This Class is used delete
class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
    
'''
def delete_data(requist, id):
    if requist.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()

        return HttpResponseRedirect('/')
'''