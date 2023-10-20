from django.shortcuts import render

# Home page views here.
def home(request):
    print("I am Home View")
    return render(request, 'mysite/home.html')


# About page views here.
def about(request):
    print("I am about view")
    return render(request, 'mysite/about.html')
