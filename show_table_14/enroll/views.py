from django.shortcuts import render
from enroll.models import Student
# Create your views here.

def studentinfo(request):
    stud = Student.objects.all()
    return render(request, 'enroll/studentdetails.html', {'stu': stud})
