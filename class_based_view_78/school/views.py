from django.shortcuts import render
from .forms import StudentForm
from django.http import HttpResponse
from django.views import View

# Create Function Based base views here.
def myfun(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)

        if fm.is_valid():
            fm.cleaned_data['name']
            fm.cleaned_data['course']
            return HttpResponse("Thank you your submit successfully")
    else:
        fm = StudentForm()
    return render(request, 'school/home.html', {'form':fm})


# Create Class Based Base views here        
class MyClassView(View):
    def get(self, request):
        fm = StudentForm()
        return render(request, 'school/home.html', {'form':fm})
    
    def post(self, request):
        fm = StudentForm(request.POST)
            
        if fm.is_valid():
            fm.cleaned_data['name']
            fm.cleaned_data['course']
            return HttpResponse("class Based views Successfully")


# ********************* One view Function/Class is render different HTML file *******************************

# Function based view function

def newfun(request, template_name):
    #template_name = 'school/news1.html'     
    template_name = template_name    
    context = {'info': 'One View function but more than showing HTML file '}
    return render(request, template_name, context)


# class Based view function
class NewsClassView(View):
    #template_name = 'school/news1.html'
    template_name = ''
    def get(self, request):
        context = {'info': 'One View function but more than showing HTML file '}
        return render(request, self.template_name, context)

