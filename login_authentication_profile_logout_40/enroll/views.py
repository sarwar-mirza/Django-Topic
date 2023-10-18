from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#signup view function start here
def user_signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)

        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your account has been created successfully !!!')
    else:
        fm = SignupForm()
    return render(request, 'enroll/signup.html', {'form':fm})
#signup view function end here



#login view function start here
def user_login(request):
    if not request.user.is_authenticated:         
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)

            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']

                user = authenticate(username = uname, password = upass)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login your successfully !!!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()            
        return render(request, 'enroll/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')
    
#login view function end here


#profile 
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html', {'name':request.user})
    else:
        return HttpResponseRedirect('/login/')

#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
