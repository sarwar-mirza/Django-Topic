from django.shortcuts import render
from .models import Student, ProxyStudent

def home(request):
    #student_data = ProxyStudent.objects.all()
    student_data = ProxyStudent.students.get_stu_roll_ranage(103, 106)        #change Manager Name 
    return render(request, 'school/home.html', {'students':student_data})
