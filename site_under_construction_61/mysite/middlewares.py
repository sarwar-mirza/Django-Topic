from django.shortcuts import render

class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        print("Call from Middleware -Before view")
        #response = self.get_response(request)
        response = render(request, 'mysite/siteuc.html')
        print("Call from Middleware -After View")
        return response