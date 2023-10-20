from django.shortcuts import render
from .models import Student
from datetime import date, time
# Create your views here.

def home(request):
    #student_data = Student.objects.all()
    
    
    #student_data = Student.objects.filter(name__exact='Sadiya')
    
    #student_data = Student.objects.filter(name__iexact='sadiya')
    
    
    
    #student_data = Student.objects.filter(name__contains='a')
      
    #student_data = Student.objects.filter(name__icontains='R')
    
    
    
    #student_data = Student.objects.filter(id__in=[2, 6, 10])
    
    #student_data = Student.objects.filter(marks__in=[70, 50])
    
    
    #student_data = Student.objects.filter(marks__gt=50)
    
    #student_data = Student.objects.filter(marks__gte=50)
    
    #student_data = Student.objects.filter(marks__lt=50)
    
    #student_data = Student.objects.filter(marks__lte=50)
    
    
    
    #student_data = Student.objects.filter(name__startswith='S')
    
    #student_data = Student.objects.filter(name__istartswith='s')
    
    
    
    #student_data = Student.objects.filter(name__endswith='a')
    
    #student_data = Student.objects.filter(name__iendswith='A')
    
    
    
    #student_data = Student.objects.filter(passdate__range=('2023-9-13', '2023-10-31'))
    
    
    #student_data = Student.objects.filter(admdatetime__date=date(2022, 12, 15))
    
    #student_data = Student.objects.filter(admdatetime__date__gt=date(2022, 12, 15))
    
    
    
    #student_data = Student.objects.filter(passdate__year=2022)
    
    #student_data = Student.objects.filter(passdate__year__gt=2022)
    
    #student_data = Student.objects.filter(passdate__month__gt=7)
    
    #student_data = Student.objects.filter(passdate__day=15)
    
    #student_data = Student.objects.filter(passdate__day__gt=15)
    
    
    #student_data = Student.objects.filter(passdate__week=7)
    
    #student_data = Student.objects.filter(passdate__week__gt=7)
    
    
    #student_data = Student.objects.filter(passdate__week_day=3)
    
    #student_data = Student.objects.filter(passdate__week_day__gt=3)
    
    
    
    #student_data = Student.objects.filter(passdate__quarter=3)
    
    
    student_data = Student.objects.filter(admdatetime__time=time(6,00))


    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students':student_data})
