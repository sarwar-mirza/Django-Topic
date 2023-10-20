"""
URL configuration for class_based_view_78 project.

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
    path('fun', views.myfun, name='home'),
    path('cl/', views.MyClassView.as_view(), name='cl'),

    #path('newsfun/', views.newfun, name='newsfun'),             # function based urls path
    path('newfun/', views.newfun, {'template_name': 'school/news1.html'}, name='newsfun'),
    path('newsfun2/', views.newfun, {'template_name': 'school/news2.html'}, name='newsfun2'),
    #********************************************************************************************

    # Class Based urls
    
    #path('newscl/', views.NewsClassView.as_view(), name='newscl'),
    path('newscl/', views.NewsClassView.as_view(template_name= 'school/news1.html'), name='newscl'),
    path('newscl2/', views.NewsClassView.as_view(template_name= 'school/news2.html'), name='newscl2'),
]
