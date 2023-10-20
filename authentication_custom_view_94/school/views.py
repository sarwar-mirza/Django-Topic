from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic.base import TemplateView
from .forms import LoginForm


class Home(TemplateView):
    template_name = 'school/home.html'

class DashBoard(TemplateView):
    template_name = 'school/dashboard.html'


# Login views here.
class User_loginView(LoginView):
    template_name = 'school/login.html'
    authentication_form = LoginForm           # css use korar jonno authentication_form = forms_name likthe hoye
    

# Logout views here
class User_logoutView(LogoutView):
    template_name = 'school/logout.html'


class User_passwordChangeView(PasswordChangeView):
    template_name = 'school/passwordchange.html'
    success_url = '/custom/changepassdone/'

class User_changepasswordDone(PasswordChangeDoneView):
    template_name = 'school/changepassworddone.html'
    

