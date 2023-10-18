from django.shortcuts import render

# Create your views here.
def learn_django(request):
    stu = {'names': ['sarwar', 'sadiya', 'tumpa']}
    return render(request, 'course/courseone.html', stu)
