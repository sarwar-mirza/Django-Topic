from django.shortcuts import render
'''
#Ex-01 session
# Set session views here.
def set_session(request):
    request.session['name'] = 'Sadiya'
    return render(request, 'student/setsession.html')

# Get session views here.
def get_session(request):
    #name = request.session.get('name')
    name = request.session.get('name', default='Guest')
    return render(request, 'student/getsession.html', {'name':name})

# Delete session views here.
def del_session(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'student/delsession.html')
'''
'''
#Ex-02 Session Methods 
# Set session views here.
def set_session(request):
    request.session['name'] = 'Sajada'
    request.session['lname'] = 'Sadiya'
    return render(request, 'student/setsession.html')

# Get session views here.
def get_session(request):
    name = request.session.get('name')
    keys = request.session.keys()           #key() method 
    items = request.session.items() 
    age = request.session.setdefault('age', 26)
    return render(request, 'student/getsession.html', {'name':name, 'keys':keys, 'items':items, 'age':age})

# Delete session views here.
def del_session(request):
    request.session.flush()
    return render(request, 'student/delsession.html')
'''


#Ex-03 session cookiw expery
# Set session views here.
def set_session(request):
    request.session['name'] = 'Sajada'
    request.session.set_test_cookie()
    request.session.set_expiry(10)
    return render(request, 'student/setsession.html')

# Get session views here.
def get_session(request):
    name = request.session.get('name')
    #print(request.session.get_session_cookie_age())
    #print(request.session.get_expiry_age())
    #print(request.session.get_expiry_date())
    #print(request.session.get_expire_at_browser_close())
    return render(request, 'student/getsession.html', {'name':name})

# Delete session views here.
def del_session(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')