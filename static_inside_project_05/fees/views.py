from django.shortcuts import render

# Create your views here.
def fees_django(request):
    return render(request, 'fees/feesone.html', {'cname': 'Django', 'charge': 30000, 'title': 'Django Fees'} )
