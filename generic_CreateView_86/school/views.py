from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

# Create your views here.
class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/modelform.html'

    success_url = '/thanks/'


class ThankTemplateView(TemplateView):
    template_name = 'school/thankyou.html'
