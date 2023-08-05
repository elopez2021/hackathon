import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
import requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .decorators import unauthenticated_user


# Create your views here.
def login(request):
    if request.method == 'POST':
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
                        user.save()

                        user = authenticate(request, username=username, password=password)
            
                        if user is not None and user.is_authenticated:
                            # User is authenticated, log them in
                            login(request, user)
                            return redirect('home')
                        else:
                            # Authentication failed, handle the error as needed
                            messages.error(request, "Invalid username or password")
                if data["data"]['isActive'] and data["data"]['isAdmin'] == False and data["data"]["isReception"] == False:
                    return redirect(reverse('home'))
        else:
            messages.error(request, 'Error en el servidor')
    return render(request, 'user/login.html')

@unauthenticated_user
def home(request):
    return render(request, 'user/dashboard.html')
