from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("getdishes/<int:restaurant_id>", views.get_dishes_by_restaurant, name="dishes_restaurant"),
]