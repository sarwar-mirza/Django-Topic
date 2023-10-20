from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create profile views here.
@login_required
def profile(request):
    return render(request, 'registration/profile.html')


# Create About Page
@staff_member_required
def about(request):
    return render(request, 'registration/about.html')

