from django.shortcuts import render
from .models import Student
from django.db.models import Avg, Sum, Min, Max, Count
# Create your views here.

def home(request):
    student_data = Student.objects.all()
    average = student_data.aggregate(Avg('marks'))
    totalcount = student_data.aggregate(Count('marks'))
    maximum = student_data.aggregate(Max('marks'))
    minimum = student_data.aggregate(Min('marks'))
    total = student_data.aggregate(Sum('marks'))

    context = {'students': student_data, 'average':average, 'totalcount':totalcount, 'maximum':maximum, 'minimum':minimum, 'total':total}

    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', context)
