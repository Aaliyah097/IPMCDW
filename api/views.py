from django.shortcuts import render
from rest_framework import generics
from . import serializers
from Main import models

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authtoken.models import Token


# полный список пользователей, можно использовать фильтрацию по ключевым полям: GET, POST
class UsersList(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filterset_fields = ['email', 'company', 'city', 'country', 'first_name',
                        'second_name', 'industry', 'is_business', 'status']


# информация по конкретному пользователю через /id: DELETE, PUT, GET
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
