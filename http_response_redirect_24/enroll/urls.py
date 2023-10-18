from django.urls import path
from . import views

urlpatterns = [
    path('regi/', views.stu_registration),
    path('successfully/', views.thankyou),
]