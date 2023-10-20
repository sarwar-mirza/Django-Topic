from django.shortcuts import render
from .models import Student
from django.db.models import Avg, Sum, Min, Max, Count
# Create your views here.

def home(request):
    #student_data = Student.objects.all()[:5]
    
    
    #student_data = Student.objects.all()[5:10]
    
    
    student_data = Student.objects.all()[:10:2]
    
    print("Return: ", student_data)
    print()
    
    return render(request, 'school/home.html', {'students':student_data})
