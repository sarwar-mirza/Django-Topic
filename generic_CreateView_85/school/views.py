from django.shortcuts import render
from .models import Student
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
# Create your views here.

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'password']
    #success_url = '/thanks/'
    

class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

class StudendDetailView(DetailView):
    model = Student

