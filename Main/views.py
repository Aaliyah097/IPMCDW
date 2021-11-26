from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

# Create your views here.


def enter_page(request):
    # user = User.objects.create(email="address@mail.domen", password="123")
    # user.save()

    # people = User.objects.all()
    # print(people)
    return render(request, 'index.html', context={})
