from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Import this decorator if you want to disable CSRF protection for testing purposes
from .models import TestInt, MyStrings
from django.views.decorators.http import require_http_methods

def home(request):
    return HttpResponse("Hello, World!")

def create_testint(request):
    new_integer = TestInt(my_integer = 5)
    new_integer.save()
    return HttpResponse("we saved it")

@csrf_exempt  # Use this decorator to disable CSRF protection for testing purposes; remove it in production
def post_string(request):
    if request.method == "POST":
        #here, the client can choose the key, but we are choosing the key. in practice, id do smth like:
        # Get the list of keys from the POST data
            # keys = request.POST.keys()
        test_str = request.GET.get('test_str') #this key must stay consistent for now
        print(test_str)
        if test_str is not None:
            try:
                print(1)
                str(test_str)
                MyStrings.objects.create(my_string = test_str) #creates a new object in MyStrings model
                return JsonResponse({"message": "Saved it"})
            except ValueError:
                print(4)
                return JsonResponse({"message": "Didnt work"})
        else:
            print(2)
            HttpResponse({"message": "Didnt work bc none"})
    else:
        print(3)
        return JsonResponse({"message": "Invalid request method"})
    
def get_strings(request):
    if request.method == "GET":
        my_strs = MyStrings.objects.all()
        my_strs_output = list(my_strs.values()) #this is how we get a list of values to output
        return JsonResponse(data=my_strs_output, safe = False) #its recommended to make safe false bc if true, it can only pass dicts
    else:
        return JsonResponse("didnt work")
    

@require_http_methods(["DELETE"])
@csrf_exempt #this is to bypass authentication bc auth is needed for deletion
def delete_this(request, string_id):
    if request.method == "DELETE":
        to_delete = MyStrings.objects.get(id = string_id)
        to_delete.delete()
        return JsonResponse({"message": "String deleted successfully"})
    else:
        return JsonResponse({"message": "oops"})
    
    
#for future ref: to send or recieve data, it's recommended to send a body, not send the data through the url
#each request has a body, and this can be in json, javascript, html, etc.. anything to send some kind of data in
#this data can be accessed using the request.body attribute of the instance of the request object
#request is an instance of the class HttpRequest that encapsulates all the information about this request