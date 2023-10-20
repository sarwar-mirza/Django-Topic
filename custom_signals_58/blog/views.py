from django.shortcuts import render, HttpResponse
from blog import signlas
# Create your views here.
def home(request):
    signlas.notification.send(sender=None, request=request, user=['sarwar', 'mithu'])
    return HttpResponse('This is home page')
