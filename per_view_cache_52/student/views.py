from django.shortcuts import render
'''
from django.views.decorators.cache import cache_page

# With cache  views here.
@cache_page(40)
def home(request):
    return render(request, 'student/home.html')

#without cache views function
def about(request):
    return render(request, 'student/about.html')
'''

def home(request):
    return render(request, 'student/home.html')


def about(request):
    return render(request, 'student/about.html')