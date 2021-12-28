from rest_framework import serializers
from Main import models
from rest_framework.renderers import StaticHTMLRenderer
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import status


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = '__all__'


class IndustrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Industry
        fields = '__all__'


