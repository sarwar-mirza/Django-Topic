from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'enroll/home.html')

#def show_details(request, my_id):
#    return render(request, 'enroll/show.html', {'id':my_id})

def show_details(request, my_id):
    if my_id == 1:
        student = {'id':my_id, 'name':'Sarwar mithu'}
    if my_id == 2:
        student = {'id':my_id, 'name':'Sadiya Hoque'}
    if my_id == 3:
        student = {'id':my_id, 'name':'Pinkey'}
    
    return render(request, 'enroll/show.html', student)

def show_subdetails(request, my_id, my_subid):
    if  my_id == 1 and my_subid == 5:
        student = {'id':my_id, 'name': 'Abu Taher', 'info':'Information in subdetails'}
    if  my_id == 2 and my_subid == 6:
        student = {'id':my_id, 'name': 'Sajada Akther', 'info':'Information in subdetails'}
    if  my_id == 3 and my_subid == 7:
        student = {'id':my_id, 'name': 'Mrs Misu', 'info':'Information in subdetails'}

    return render(request, 'enroll/show.html', student)

