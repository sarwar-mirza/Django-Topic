from django.urls import path
from  . import views

urlpatterns = [
    path('forms/', views.studentdetails),
    path('widget/', views.learn_widget),
]