from django.urls import path
from . import views
urlpatterns = [
    path('studata/', views.studentinfo),
]