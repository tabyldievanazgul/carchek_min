from django.db import models
# from django.contrib.auth.models import AbstractUser
import os
from django.db.models import Count
# Create your models here.


class Car(models.Model):
    number = models.CharField(max_length=100)
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')


    def __str__(self):
        return f'{self.marka}--{self.model}'

#
# class User(AbstractUser):
#     name = models.CharField(
#         verbose_name='Name of User',
#         blank=True, max_length=15
#     )
#     def __str__(self):
#         return f'{self.username}'

class Use(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    car_id = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name='cars'
    )
    def __str__(self):
        return f'{self.car_id}--{self.start_date}'


