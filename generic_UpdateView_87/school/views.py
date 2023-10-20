from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView

# Create  views here.
class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanks/'

class ThankCreateView(TemplateView):
    template_name = 'school/thanks.html'


# Update Views here
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanksupdate/'

class ThankUpdateView(TemplateView):
    template_name = 'school/update.html'

