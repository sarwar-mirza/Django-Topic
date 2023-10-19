from django.shortcuts import render

# Create your views here.
def mycount(request):
    count = request.session.get('count', 0)
    newCount = count + 1                     #variable name plus increment
    request.session['count'] = newCount
    return render(request, 'count/home.html', {'newCount': newCount})
