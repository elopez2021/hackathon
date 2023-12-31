# Generated by Django 4.2.4 on 2023-08-05 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0002_restaurantemployee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('dish_id', models.AutoField(primary_key=True, serialize=False)),
                ('dish_name', models.CharField(max_length=100)),
                ('dish_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dish_description', models.TextField()),
                ('dish_category', models.CharField(max_length=100)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='restaurantapp.restaurant')),
            ],
        ),
    ]
