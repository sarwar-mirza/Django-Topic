from django.shortcuts import render
from .models import Student

'''
# Modify the inital Queryset  your views here.
def home(request):
    #student_data = Student.objects.all()
    student_data = Student.students.all()        #change Manager Name 
    return render(request, 'school/home.html', {'students':student_data})
'''

# Add Extra Manager  your views here.
def home(request):
    #student_data = Student.objects.all()
    student_data = Student.students.get_stu_roll_ranage(103, 108)        #change Manager Name 
    return render(request, 'school/home.html', {'students':student_data})
