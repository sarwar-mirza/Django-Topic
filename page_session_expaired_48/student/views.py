from django.shortcuts import render, HttpResponse

# Set Expaired views here.
def set_expaired(request):
    request.session['name'] = 'Sadiya'
    return render(request, 'student/setexpaired.html')

# Set Expaired views here.
def get_expaired(request):
    if 'name' in request.session:                   #setting.py->SESSION_COOKIE_AGE = 10 -> views.py->condition (time limit)
        name = request.session['name']
        request.session.modified = True             # page modified hole time duration bere jabe
        return render(request, 'student/getexpaired.html', {'name':name})
    else:
        return HttpResponse('Your session has Expaired....')
# Set Expaired views here.
def del_expaired(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delexpaired.html')