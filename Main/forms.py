from django import forms
from .models import User
from django.forms import ModelForm


class SignInForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'company', 'country',
                  'address', 'zipcode', 'city', 'phone_1',
                  'website', 'firstname', 'lastname', 'post',
                  'currency', 'industry']