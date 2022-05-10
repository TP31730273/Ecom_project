from django.shortcuts import HttpResponse, redirect


class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Brother middleware")
        # One-time configuration and initialization.

    def __call__(self, request):
        
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        print(self.get_response,"kdkljfkljfkdjfkdfjkdkfdkfdj")
        

        # Code to be executed for each request/response after
        # the view is called.

        return response

    # def process_view(request,*args,**kwargs):
    #     return None

    def process_exception(self,request,exception):
        print(exception,"949284024802498242420482942084209420")
        return HttpResponse(exception)

    def process_template_response(self,request,response):
       
        return response




def seller_auth(get_response):
    
    def my_function(request):
        if not request.session.get('seller_email'):
            return redirect('SellerLoginView')

        response=get_response(request)
       
        return response
    return my_function

def customer_auth(get_response):
    
    def my_function(request):
        if not request.session.get('user_email'):
            return redirect('LoginView')
            
        response=get_response(request)

        return response
    return my_function