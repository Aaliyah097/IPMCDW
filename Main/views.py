from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def enter_page(request):
    return render(request, 'index.html', context={})

def recovery_page(request):
    return render(request, 'recovery.html', context={})

def lk_page(request):
    return render(request, 'lk.html', context={})