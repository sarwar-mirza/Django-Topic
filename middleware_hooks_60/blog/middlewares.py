from django.shortcuts import HttpResponse


class MyProcessMiddleware:
    def __init__(self, get_rsponse):
        self.get_response = get_rsponse
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    #prcess_view
    def process_view(request, *args, **kwargs):
        print("This Process view - Before view")
        return HttpResponse('This is before view')     # view function call korbe na 
        #return None
    
class MyExceptionMiddleware:
    def __init__(self, get_rsponse):
        self.get_response = get_rsponse
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    #prcess_exception
    def process_exception(self, request, exception):
        print("Exception Occured")
        msg = exception
        return HttpResponse(msg)     # view function kono error pelei tobe ai function kaj korbe


class MyTemplateResponseMiddleware:
    def __init__(self, get_rsponse):
        self.get_response = get_rsponse
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    #prcess_template_rsponse
    def process_template_response(self, request, response):
        print("Process Template Response from Middleware")
        response.context_data['name']= 'Sadiya'
        return response
       
        