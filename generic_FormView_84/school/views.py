from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContratForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

# Create your views here.
class ContractFormView(FormView):
    template_name = 'school/contract.html'
    form_class = ContratForm
    success_url = '/thankyou/'

    def form_valid(self, form):
        nm = form.cleaned_data['name']
        em = form.cleaned_data['email']
        msg = form.cleaned_data['msg']
        return super().form_valid(form)
        #return HttpResponse('Successfully fill up Form')

class ThankyouTemplateView(TemplateView):
    template_name = 'school/thankyou.html'
    
