from django.shortcuts import render, HttpResponseRedirect 
from enroll.forms import SginupForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group
# Create your views here.

#signup form views function
def user_signup(request):
    if request.method == 'POST':
        fm = SginupForm(request.POST)

        if fm.is_valid():
            messages.success(request, 'Your account has been created successfully !!!')
            user = fm.save()
            group = Group.objects.get(name='Editor')
            user.groups.add(group)
           
    else:
        fm = SginupForm()
    return render(request, 'enroll/signup.html', {'form':fm})

#login form views function
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


#prfile views function
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance=request.user)

                users_data = User.objects.all()
            else:
                fm = EditUserProfileForm(request.POST, instance=request.user)
                users_data = None

            if fm.is_valid():
                messages.success(request, 'Your profile is Update')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users_data = User.objects.all()
            else:
                fm = EditUserProfileForm(instance=request.user)
                users_data = None

        return render(request, 'enroll/profile.html', {'name': request.user.username, 'form':fm, 'users':users_data})
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
                messages.success(request, 'Profile update successfully done !')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepassword.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    

# user detail
def user_detail(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=pi)
        return render(request, 'enroll/userdetails.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
# User Deshbort

def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/dashboard.html', {'name':request.user.username})
    else:
        return HttpResponseRedirect('/profile/')
