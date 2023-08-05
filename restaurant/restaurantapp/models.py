from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    main_contact = models.CharField(max_length=100)
    limit_time = models.TimeField()
    city_labor = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class RestaurantEmployee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='employees')

class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True)
    dish_name = models.CharField(max_length=100)
    dish_price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_description = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')
    dish_category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.dish_name