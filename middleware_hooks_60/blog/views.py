from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse


# process_view views here.
def home(request):
    print("I am Home view")
    return HttpResponse("This is Home Page")


# process_exception views here.
def excp(request):
    print("I am Excp view")
    a = 10/0
    return HttpResponse("This is Excp Page")

# process_template_response views here.
def user_info(request):
    print("I am user inof view")
    context = {'name': 'sarwar'}
    return TemplateResponse(request, 'blog/user.html', context)