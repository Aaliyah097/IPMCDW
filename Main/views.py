from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def enter_page(request):
    return render(request, 'index.html', context={})
