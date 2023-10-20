"""
URL configuration for redirect_view_80 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TemplateView.as_view(template_name='school/home.html'), name='blnkhome'),
    path('home/', views.RedirectView.as_view(url='/'), name='home-p'),
    path('index/', views.RedirectView.as_view(pattern_name='home-p'), name='index'),
    
    #External urls difine
    #path('geekyshows/', views.RedirectView.as_view(url='http://www.geekyshows.com'), name='go-to-geekyshows'),
    
    path('geekyshows/', views.SarwarMithuRedirectView.as_view(), name='go-to-geekyshows'),

    # ex-02 -> ex-02 page dekabe(only integer value)
    path('home/<int:pk>/', views.MithuRedirectView.as_view(), name='mithu'), # Ex-01
    path('mithu/<int:pk>/', views.TemplateView.as_view(template_name='school/home.html'), name='mindex'), # Ex-02


    # ex-02 -> ex-02 page dekabe(only text value)
    path('home/<slug:post>/', views.MithuRedirectView.as_view(), name='mithu'), # Ex-01
    path('<slug:post>/', views.TemplateView.as_view(template_name='school/home.html'), name='mindex'), # Ex-02

]
