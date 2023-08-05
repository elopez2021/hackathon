from django.db import models

# Create your models here.


status_choice=(
        ('process','En Proceso'),
        ('accepted','Aceptado'),
        ('packed','Empacado'),
        ('shipped','Transportado'),
        ('delivered','Entregado'),
)


class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True)
    dish_name = models.CharField(max_length=100)
    dish_price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_description = models.TextField()
    dish_category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.dish_id


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
