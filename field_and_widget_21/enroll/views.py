from django.shortcuts import render
from enroll.forms import StudentForm, WidgetForm
# Create your views here.

def studentdetails(request):
    fm = StudentForm()
    return render(request, 'enroll/stuform.html', {'form':fm})

def learn_widget(request):
    wg = WidgetForm()
    return render(request, 'enroll/widgetinfo.html', {'form':wg})


