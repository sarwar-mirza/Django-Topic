from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:id>/', views.UserDeleteView.as_view(), name='deletedata'),
    path('update/<int:id>/', views.UserUpdateView.as_view(), name='updatedata'),
]