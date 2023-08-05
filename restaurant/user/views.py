from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from login.decorators import unauthenticated_user
from restaurantapp.models import *

# Create your views here.
@unauthenticated_user
def home(request):
    restaurant = Restaurant.objects.all()
    context = {'restaurants': restaurant}
    return render(request, 'user/dashboard_user.html', context)

@unauthenticated_user
def get_dishes_by_restaurant(request, restaurant_id):
    dishes = Dish.objects.filter(restaurant=restaurant_id).values('dish_id', 'dish_name', "dish_price")
    dishes_list = list(dishes)
    return JsonResponse({'dishes': dishes_list})
