'''
# Function Based middleware
def my_middleware(get_response):
    print('One time initialization')
    def my_function(request):
        print('This is before view')
        response = get_response(request)
        print('This is after view')
        return response
    return my_function
'''
'''
# class based middleware
class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Initialization")

    def __call__(self, request):
        print("This is before view")
        response = self.get_response(request)
        print("This is after view")
        return response
'''

class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Brother Initialization")

    def __call__(self, request):
        print("This is Brother before view")
        response = self.get_response(request)
        print("This is Brother after view")
        return response
    
class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Father Initialization")

    def __call__(self, request):
        print("This is Father before view")
        response = self.get_response(request)
        print("This is Father after view")
        return response
    
class MummyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Mummy Initialization")

    def __call__(self, request):
        print("This is Mummy before view")
        response = self.get_response(request)
        print("This is Mummy after view")
        return response