from django.shortcuts import render
from rest_framework import generics
from . import serializers
from Main import models

import json

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
from django_filters.rest_framework import DjangoFilterBackend
from django.forms.models import model_to_dict
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class UsersList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    filterset_fields = ['email', 'company', 'country', 'city', 'industry', 'is_verified']

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.data)
        return self.create(request, *args, **kwargs)


class UserDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(['POST'])
def enter_account(request):
    data = request.POST.dict()

    print(data)

    password = data.get('password', None)
    email = data.get('email', None)

    try:
        user = models.User.objects.get(email=email, password=password)
        serializer = serializers.UserSerializer(user)
        request.session['token'] = user.token
    except models.User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)
