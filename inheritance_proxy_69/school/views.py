from django.shortcuts import render
from .models import ExamCenter, MyExamCenter

# Create your views here.
def home(request):
    exam_center = ExamCenter.objects.all()
    my_examCenter = MyExamCenter.objects.all()
    return render(request, 'school/home.html', {'exams':exam_center, 'myexams':my_examCenter})
