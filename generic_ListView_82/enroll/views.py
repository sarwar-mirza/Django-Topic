from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Student
from django.views.generic.list import ListView
'''
# Default ListView.
class StudentListView(ListView):
    model = Student          # method model = create_models_name

    #template_name_suffix = '_get'    # mehtod
    #ordering = ['name']
'''


# Custom ListView.
class StudentListView(ListView):
    model = Student          # method model = create_models_name

    template_name = 'enroll/custom.html'    # custom define HTML File
    context_object_name = 'students'       # custom define context Name

    def get_queryset(self):
        return Student.objects.filter(course='python')
    
    
    def get_context_data(self, *args,  **kwargs):
        context =  super().get_context_data( *args, **kwargs)
        context['freshers'] = Student.objects.all().order_by('name')
        return context
    

    def get_template_names(self):          # setup browser setting-> moretools -> application -> cookie
        if self.request.COOKIES['user'] == 'Sadiya':
            template_name = 'enroll/sadiya.html'
        else:
            template_name = self.template_name
        return [template_name]
    
'''
    def ger_template_names(self):
        if self.request.user.is_superuser:
            template_name = 'enroll/superuser.html'
        elif self.request.user.is_staff:
            template_name = 'enroll/staff.html'
        else:
            template_name = self.template_name
        return [template_name]
'''