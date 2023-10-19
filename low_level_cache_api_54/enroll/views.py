from django.shortcuts import render
from django.core.cache import cache

#ex-01
# get, set views here.
def home(request):
    mv = cache.get('movie', 'has_expaired')     #cache.get('key', 'default_value')
    if mv == 'has_expaired':
        cache.set('movie', 'The manjhi', 40)    #cache.set('key', 'value')
        mv = cache.get('movie')
    return render(request, 'enroll/home.html', {'mv':mv})


#ex-02
# get_or_set() method

#def home(request):
    #mv = cache.get_or_set('fees', '4000 tk only',30)
#    mv = cache.get_or_set('fees', '3003 tk only',30, version=2)
#    return render(request, 'enroll/home.html', {'mv':mv})

#ex-03
#passing dictionary

#def home(request):
#    data = {'name': 'sadiya', 'roll':101}
#    cache.set_many(data, 30)
#    sv = cache.get_many(data)
#    return render(request, 'enroll/home.html', {'stu':sv})


#ex-04
# delete(key)  metheo
#def home(request):
#    cache.delete('roll')
#    return render(request, 'enroll/home.html')


#ex-05
#clear() mehtod 
#def home(request):
#    cache.clear()
#    return render(request, 'enroll/home.html')