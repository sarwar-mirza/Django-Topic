from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create profle views here.
class LoginTemplateView(TemplateView):
    template_name = 'registration/profile.html'

# Create about views here
class AboutTemplateView(TemplateView):
    template_name = 'registration/about.html'
