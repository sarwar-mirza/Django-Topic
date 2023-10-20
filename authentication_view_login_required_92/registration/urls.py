from django.urls import path
from registration import views

urlpatterns = [
    path('profile/', views.LoginTemplateView.as_view(), name='profile'),
]