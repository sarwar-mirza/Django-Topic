from django.urls import path
from . import views
urlpatterns = [
    path('student/', views.student_form),
    path('teacher/', views.teacher_form),
]