from django.db import models
from restaurantapp.models import Dish
from django.contrib.auth.models import User

# Create your models here.


status_choice=(
        ('process','In Process'),
        ('accepted','Accepted'),
        ('packed','Packed'),
        ('shipped','Transported'),
        ('delivered','Delivered'),
)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=255, null=True)
    order_status=models.CharField(choices=status_choice,default='process',max_length=150)

    def __str__(self):
        return str(self.order_id)

class CartOrderItems(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE, related_name="cart_items")
    dish=models.ForeignKey(Dish, on_delete=models.CASCADE)
    qty=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField()

    class Meta:
        verbose_name_plural='Order Items'
    
    def __str__(self): 
        return str(self.order.order_id)
