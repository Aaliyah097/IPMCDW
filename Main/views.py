from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import SignInForm, SignUpForm, EditProfileForm
from api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
import requests

# Create your views here.


def enter_page(request):
    context = {'is_authorized' : False}
    if 'email' in request.session:
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

    form = EditProfileForm(
        initial={
            'email': user.email,
            'company': user.company,
            'post': user.post,
            'phone_1': user.phone_1,
            'phone_2': user.phone_2,
            'website': user.website,
            'post': user.post,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'industry': user.industry,
            'description': user.description,
        }
    )
    print(user.email)

    context = {'user': serializer.data, 'form': form}

    return render(request, 'lk.html', context)


def sign_out(request):
    if 'email' in request.session:
        del request.session['email']

    return redirect("/")

