"""
URL configuration for test_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import my_test.views

#to run server -> python3 manage.py runserver

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #the home function is defined in views, and the path is the default path
    path('', my_test.views.home, name = 'home'),

    path('test_int/', my_test.views.create_testint, name = 'testing'),

    path('post_string/', my_test.views.post_string, name = 'post_string'),

    path('get_strs/', my_test.views.get_strings, name = 'get_strs'),

    path('delete_this/<int:string_id>', my_test.views.delete_this, name = 'delete_string'),

    path('new_user/', my_test.views.new_user, name = 'new_user'),
]

