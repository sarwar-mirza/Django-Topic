from django.urls import path
from school import views

urlpatterns = [
    path('dashboard/', views.DashBoard.as_view(), name='dashboard'),
    path('login/', views.User_loginView.as_view(), name='login'),
    path('logout/', views.User_logoutView.as_view(), name='logout'),
    path('changepass/', views.User_passwordChangeView.as_view(), name='changepass'),
    path('changepassdone/', views.User_changepasswordDone.as_view(), name='changepassdone'),

]