from django.shortcuts import render

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
    return render(request, 'user/login.html')