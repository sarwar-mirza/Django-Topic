from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
# Ex-03
class HomeTemplateView(TemplateView):
    template_name='school/home.html'         # override in TemplateView

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['name'] = 'Sadiya'
        context['roll'] = 101
        return context