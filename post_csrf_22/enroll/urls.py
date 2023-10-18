from django.urls import path
from . import views

urlpatterns = [
    path('cross/', views.regi_form),
]