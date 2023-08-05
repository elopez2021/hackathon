import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
import requests


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
            field2 = data['data']
            # Process the data as needed
            if field1 == False:
                messages.error(request, data['error'])
            else:
                if field2['isActive'] and field2['isAdmin'] == False and field2['isReception'] == False:
                    return redirect(reverse('home'))
        else:
            messages.error(request, 'Error en el servidor')
    return render(request, 'user/login.html')

def home(request):
    return render(request, 'user/dashboard.html')
