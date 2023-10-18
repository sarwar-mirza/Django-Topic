from django.urls import path
from . import views

urlpatterns = [
    path('regi/', views.student_regi),
]