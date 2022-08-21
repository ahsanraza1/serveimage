"""serve_image URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from serve_image_api import views
from account import views as acc_view

from rest_framework.authtoken import views as authviews
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/account/all', acc_view.show_users),


    
        # Request body should have:
        #     username : // username
        #     email : // email ( unique )
        #     password : // password
        
        # Response:
        #     {"username":"","email":"","password":""}
        # Errors:
        #     {"error":{"// field name //":["error message"]}}

    path('api/account/register', acc_view.register),

        # Request body should have:
        #     username : // send email here 
        #     password : // password
        
        # Response:
        #     {"token":"...."}
        # Errors:
        #     {"non_field_errors":["Unable to log in with provided credentials."]}
        #     {"username":["This field is required."]}
        #     {"username":["This field may not be blank."],"password":["This field may not be blank."]}
        #     {"error":{"// field name //":["error message"]}}
    
    path('api-token-auth/', authviews.obtain_auth_token),
    

    path('home/', views.home),
]
