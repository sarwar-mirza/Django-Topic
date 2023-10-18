from django.shortcuts import render

# Create your views here.
def fees_django(request):
    fees = '45000'
    cname = {'fe':fees}
    return render(request, 'fees/feesone.html', cname)
def fees_python(request):
    fees = '40000'
    cname = {'py':fees}
    return render(request, 'fees/feestwo.html', cname)
