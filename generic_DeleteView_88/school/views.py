from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

# CreateView views here.
class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/modelform.html'
    success_url = '/thanks/'

class StudentThankCreateView(TemplateView):
    template_name = 'school/thankyou.html'

# UpdateView views here
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/modelform.html'
    success_url = '/thankupdate/'

class StudentThankUpdateView(TemplateView):
    template_name = 'school/update.html'

# DeleteView views here
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'school/studel.html'
    success_url = '/create/'



