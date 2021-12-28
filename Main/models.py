from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Industry(models.Model):
    CHOICES = (
        (0, 'Food'),
        (1, 'Finance'),
        (2, 'IT'),
    )

    name = models.IntegerField(
        choices=CHOICES,
    )

    def __str__(self):
        return self.CHOICES[self.name][1]


class User(models.Model):
    STATUS_VARS = [
        (1, 'Visitor'),
        (2, 'User'),
        (3, 'Premium'),
        (4, 'Vip'),
        (4, 'Admin'),
    ]

    CURRENCY_VARS = (
        (1, "EUR"),
        (2, 'USD'),
        (3, 'RUB'),
    )

    COUNTRY_VARS = (
        (1, "Russia"),
        (2, 'USA'),
        (3, 'Italy'),
        (3, 'Germany'),
    )

    email = models.EmailField(unique=True, default='')
    password = models.CharField(max_length=50, default='')
    company = models.CharField(max_length=100, default='', blank=True)
    country = models.IntegerField(choices=COUNTRY_VARS, default=1)
    address = models.CharField(max_length=150, default='', blank=True)
    zipcode = models.CharField(max_length=20, default='', blank=True)
    city = models.CharField(max_length=20, default='', blank=True)
    phone_1 = models.CharField(max_length=20, default='', blank=True)
    phone_2 = models.CharField(max_length=20, default='', blank=True)
    website = models.CharField(max_length=50, default='', blank=True)
    firstname = models.CharField(max_length=50, default='', blank=True)
    lastname = models.CharField(max_length=50, default='', blank=True)
    post = models.CharField(max_length=50, default='', blank=True)
    industry = models.ManyToManyField(Industry, blank=True)
    currency = models.IntegerField(choices=CURRENCY_VARS, default=1)
    is_business = models.BooleanField(default=False)
    balance = models.FloatField(default=0)
    status = models.IntegerField(choices=STATUS_VARS, default=1)
    views_count = models.PositiveIntegerField(default=0)
    description = models.TextField(default='Hi!, Welcome to my IBCA page!')
    created_at = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=64, default='', blank=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.firstname + " " + self.lastname + f" ({self.company})"


class ViewNote(models.Model):
    ip = models.GenericIPAddressField(max_length=50)
    user_id = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip} ({self.user_id})"


