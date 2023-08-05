from django.db import models
from restaurantapp.models import Dish

# Create your models here.


status_choice=(
        ('process','En Proceso'),
        ('accepted','Aceptado'),
        ('packed','Empacado'),
        ('shipped','Transportado'),
        ('delivered','Entregado'),
)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=100)
    customer_id = models.IntegerField()
    address = models.CharField(max_length=255, null=True)
    order_status=models.CharField(choices=status_choice,default='process',max_length=150)

    def __str__(self):
        return self.order_id

class CartOrderItems(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    dish=models.ForeignKey(Dish, on_delete=models.CASCADE)
    qty=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField()

    class Meta:
        verbose_name_plural='Order Items'
    
    def __str__(self): 
        return self.order.order_id
