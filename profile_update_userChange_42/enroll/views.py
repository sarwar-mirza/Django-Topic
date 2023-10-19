from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import SignupForm, EditUserProfileForm
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.

#signup views function
def user_signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)

        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your account has been created successfully !!!')
    else:
        fm = SignupForm()
    return render(request, 'enroll/signup.html', {'form':fm})

#login view function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)

            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']

                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successfully done !!!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

#profile view function
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditUserProfileForm(request.POST, instance=request.user)

            if fm.is_valid():
                messages.success(request, 'Your profile updated !!!')
                fm.save()
        else:
            fm = EditUserProfileForm(instance = request.user)
        return render(request, 'enroll/profile.html', {'name': request.user, 'form':fm})
    else:
        return HttpResponseRedirect('/login/')

#logout views function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#change password with old password
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)

            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password change successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepassword.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
