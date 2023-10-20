from typing import Any
from django import http
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Ex-01
# Create profle views here.
@method_decorator(login_required, name='dispatch')
class LoginTemplateView(TemplateView):
    template_name = 'registration/profile.html'

    

# Create about views here
@method_decorator(staff_member_required, name='dispatch')
class AboutTemplateView(TemplateView):
    template_name = 'registration/about.html'

    
'''   
# Ex-02
# Create profle views here.
class LoginTemplateView(TemplateView):
    template_name = 'registration/profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch( *args, **kwargs)

# Create about views here
class AboutTemplateView(TemplateView):
    template_name = 'registration/about.html'

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch( *args, **kwargs)
'''
