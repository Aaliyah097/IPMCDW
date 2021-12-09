from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import SignInForm, SignUpForm
from api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
import requests

# Create your views here.


def enter_page(request):
    context = {'is_authorized' : False}
    if 'token' in request.session:
        context['is_authorized'] = True

    return render(request, 'index.html', context)


def sign_in_page(request):
    form = SignInForm()
    context = {'form': form}
    return render(request, 'sign_in_page.html', context)


def sign_up_page(request):
    form = SignUpForm()
    context = {'form': form}
    return render(request, 'sign_up_page.html', context)


def recovery_page(request):
    return render(request, 'recovery.html', context={})


def lk(request, pk):

    user = User.objects.get(id=pk)
    serializer = UserSerializer(user)

    context = {'user': serializer.data}

    return render(request, 'lk.html', context)


def sign_out(request):
    if 'token' in request.session:
        del request.session['token']

    return redirect("/")
