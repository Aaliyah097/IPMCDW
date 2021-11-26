from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(models.Model):
    STATUS_VARS = [
        (1, 'visitor'),
        (2, 'user'),
        (3, 'premium'),
        (4, 'vip'),
        (4, 'admin'),
    ]

    CURRENCY_VARS = [
        (1, 'EUR'),
        (2, 'USD'),
        (3, 'RUB'),
    ]

    email = models.EmailField(unique=True, default='')
    password = models.CharField(max_length=50, default='')
    company = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=150, default='', blank=True)
    postal_code = models.CharField(max_length=20, default='', blank=True)
    city = models.CharField(max_length=20, default='')
    phone_1 = models.CharField(max_length=20, default='', blank=True)
    phone_2 = models.CharField(max_length=20, default='', blank=True)
    website = models.CharField(max_length=50, default='', blank=True)
    first_name = models.CharField(max_length=50, default='')
    second_name = models.CharField(max_length=50, default='')
    post = models.CharField(max_length=50, default='', blank=True)
    industry = models.TextField(default='', blank=True)
    currency = models.IntegerField(choices=CURRENCY_VARS, default=1)
    is_business = models.BooleanField(default=False)
    balance = models.FloatField(default=0)
    status = models.IntegerField(choices=STATUS_VARS, default=1)
    views_count = models.PositiveIntegerField(default=0)
    description = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=64, default='', blank=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.first_name + " " + self.second_name + " " + self.company
