import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
import requests
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout

from .decorators import unauthenticated_user


# Create your views here.
def login_view(request):
    if request.method == 'POST' and request.user.is_authenticated == False:
        username = request.POST.get("username")
        password = request.POST.get("password")
        url = 'https://hackathon.voiceteamcall.com?token=dGVhbTEyOjkwcjcyMzh6eQ==' 
        payload = {'username': username, 'password': password} 
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            data = response.json()
            # Access the data fields
            field1 = data['success']

            if field1 == False:
                messages.error(request, data['error'])
            else:
                if data.get('success', True):
                # If authentication is successful, check if the user exists in Django database
                    try:
                        user = User.objects.get(username=username)
                    except User.DoesNotExist:
                        # If the user does not exist, create one using the API response data
                        user = User(username=username)
                        user.set_unusable_password()
                        user.external_api_authenticated = True  # Flag to indicate the user was authenticated through the API
                        if data["data"]["isAdmin"] == True:
                            user.is_staff = True
                        group = Group.objects.get(name='supervisor')
                        user.groups.add(group)
                        user.save()

                if user is not None and user.is_authenticated:
                    login(request, user)
            
                if data["data"]['isActive'] and data["data"]['isAdmin'] == False and data["data"]["isReception"] == False:
                    return redirect("user/")
                elif data["data"]['isActive'] and data["data"]['isAdmin']:
                    return redirect("admin/")
                elif data["data"]['isActive'] and data["data"]['isReception']:
                    return redirect("admin/") 
        else:
            messages.error(request, 'Error en el servidor')
    return render(request, 'user/login.html')



@unauthenticated_user
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

