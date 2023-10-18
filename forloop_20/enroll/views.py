from django.shortcuts import render
from enroll.forms import StudentForm, HiddenForm
# Create your views here.

def studentdetails(request):
    fm = StudentForm()
    return render(request, 'enroll/stuform.html', {'form':fm})

def hideinformation(request):
    hf = HiddenForm()
    return render(request, 'enroll/hiddenloop.html', {'form': hf})
