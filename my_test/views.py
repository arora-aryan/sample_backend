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
        test_str = request.GET.get('test_str')
        print(test_str)
        if test_str is not None:
            try:
                print(1)
                str(test_str)
                MyStrings.objects.create(my_string = test_str)
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
        my_strs_output = list(my_strs.values())
        return JsonResponse(data=my_strs_output, safe = False)
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