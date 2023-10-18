from django.shortcuts import render

# Create your views here.
def learn_django(request):
    cname = 'Django'
    seats = 10
    django_ditails = {'nm':cname, 'se':seats}
    return render(request, 'course/courseone.html', django_ditails)

def learn_python(request):
    cname = 'Python'
    seats = 5
    python_details = {'nm': cname, 'st': seats}
    return render(request, 'course/coursetwo.html', python_details)

