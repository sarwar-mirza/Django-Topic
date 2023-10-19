from django.shortcuts import render
from datetime import datetime, timedelta

# Set cookie views here.
def set_cookie(request):
    response = render(request, 'student/setcookie.html')
    #response.set_cookie('name', 'mithu')
    #response.set_cookie('name', 'mithu', max_age=120)
    response.set_cookie('name', 'mithu', expires=datetime.utcnow()+timedelta(days=2))
    return response

#Get cookie views
def get_cookie(request):
    #name = request.COOKIES['name']
    #name = request.COOKIES.get('name')
    name = request.COOKIES.get('name', 'Guest')
    return render(request, 'student/getcookie.html', {'name':name})

# Delete cookie views here.
def del_cookie(request):
    response = render(request, 'student/delcookie.html')
    response.delete_cookie('name')
    return response


'''
Ex-02  (create signed cookie)
def set_cookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_signed_cookie('name', 'mithu',salt='nm', expires=datetime.utcnow()+timedelta(days=2))
    return response

def get_cookie(request):
    name = request.get_signed_cookie('name', salt='nm', default='Guest')
    return render(request, 'student/getcookie.html', {'name':name})

def del_cookie(request):
    response = render(request, 'student/delcookie.html')
    response.delete_cookie('name')
    return response
'''

