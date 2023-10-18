from django.shortcuts import render

# Create your views here.
def learn_django(request):
    cname = 'Django'
    duration = '4 Months'
    seates = 10
    django_ditails = {'nm':cname, 'du':duration, 'se':seates}
    return render(request, 'course/courseone.html', django_ditails)

def learn_python(request):
    cname = 'python'
    duration = '4 Months'
    seates = 10
    python_ditails = {'nm':cname, 'du':duration, 'se':seates}
    return render(request, 'course/coursetwo.html', python_ditails)
