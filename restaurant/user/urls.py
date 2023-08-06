from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("getdishes/<int:restaurant_id>", views.get_dishes_by_restaurant, name="dishes_restaurant"),
    path("past-orders/", views.getPastOrders, name="previous_orders"),
    path("create-order/", views.createOrder, name="create-order")
]