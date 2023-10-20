from typing import Any
from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# DetailView here.
class StudentDetaiView(DetailView):
    model = Student

    template_name = 'school/singledetail.html'
    #context_object_name = 'stu'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['all_student'] = Student.objects.all()
        return context

#ListView here
class StudentListView(ListView):
    model = Student
