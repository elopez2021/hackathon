from django.db import models

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

    