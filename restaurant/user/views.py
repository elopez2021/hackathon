from django.shortcuts import render
from login.decorators import unauthenticated_user

# Create your views here.
@unauthenticated_user
def home(request):
    return render(request, 'user/dashboard.html')
