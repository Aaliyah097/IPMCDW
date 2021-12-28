import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Industry, ViewNote
from .forms import SignInForm, SignUpForm, EditProfileForm, FilterUserForm
from api.serializers import UserSerializer, IndustrySerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F
from rest_framework.response import Response
from rest_framework import status
import requests

# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


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

    is_owner = False
    is_authorized = False

    if 'email' in request.session:
        is_authorized = True
        if request.session['email'] == user.email:
            is_owner = True

    user_ip = get_client_ip(request)
    try:
        note = ViewNote.objects.get(ip=user_ip, user_id=user.id)
    except ViewNote.DoesNotExist:
        User.objects.filter(id=user.id).update(views_count=F("views_count") + 1)
        note = ViewNote.objects.create(ip=user_ip, user_id=user)
        note.save()

    context = {'user': user, 'is_owner': is_owner, 'is_authorized': is_authorized}

    return render(request, 'lk.html', context)


def sign_out(request):
    if 'email' in request.session:
        del request.session['email']

    return redirect("/")


def edit_profile_page(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user)
    form = EditProfileForm(instance=user)
    is_owner = False
    is_authorized = False

    if 'email' in request.session:
        is_authorized = True
        if request.session['email'] == user.email:
            is_owner = True

    context = {'user': user, 'form': form, 'is_owner': is_owner, 'is_authorized': is_authorized}

    if is_owner:
        return render(request, 'edit_profile.html', context)
    else:
        return redirect("/")


def companies(request):
    users = User.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(users, 2)

    user_form = FilterUserForm()

    is_owner = False
    is_authorized = False

    if 'email' in request.session:
        is_authorized = True
        user = User.objects.get(email=request.session['email'])
        if user:
            is_owner = True
    else:
        user = None

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'all_company.html', {'users': users, 'is_owner': is_owner, 'user': user, 'is_authorized': is_authorized, 'form' : user_form})



