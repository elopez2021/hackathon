import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from login.decorators import unauthenticated_user
from restaurantapp.models import *
from .models import *

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

@unauthenticated_user
def getPastOrders(request):
    orders = Order.objects.filter(user=request.user)
    cart_order_items = CartOrderItems.objects.filter(order__user=request.user)
    context = {'orders': orders, "dishes":cart_order_items}
    return render(request, 'user/pastorder.html')

@unauthenticated_user
def createOrder(request):
    if request.method == 'POST' and request.user.is_authenticated:
        order = Order.objects.create(user=request.user)
        selected_dishes_json = request.POST.get('selected_dishes')
        selected_dishes = json.loads(selected_dishes_json)
        for dish in selected_dishes:
            dish_id = dish['id']
            dish_name = dish['name']
            dish_price = float(dish['price'])
            order_item = CartOrderItems.objects.create(order=order, dish=dish)

            total_price += dish_price  
        order.order_total = total_price          
        order.save()
    
    return render(request, 'user/dashboard_user.html')