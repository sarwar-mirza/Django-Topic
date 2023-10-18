from django.shortcuts import render
from enroll.forms import StudentForm
# Create your views here.

def registration(request):
    fm = StudentForm(auto_id=True, label_suffix=' ')
    fm.order_fields(field_order=['email', 'name', 'father_name', 'mother_name'])
    return render(request, 'enroll/form.html', {'form':fm})
