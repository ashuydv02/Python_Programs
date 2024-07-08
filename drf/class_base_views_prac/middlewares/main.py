from django.http import HttpResponse


class SimpleMiddleWare:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwds):
        print("MiddleWare is Called...")
        response = self.get_response(request)
        return response
    
    def simple_response(get_response):         
        def middleware(request):
            return HttpResponse("The permission is not granted to create a user...")
        return middleware
    