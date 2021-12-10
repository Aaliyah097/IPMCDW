from django import forms
from django.forms import widgets
from django.forms.widgets import Widget
from .models import User
from django.forms import ModelForm


class SignInForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    
        widgets = {
            'email': forms.TextInput(attrs={'class': 'sign_in_forms'}),  # or whatever class you want to apply
            'password': forms.TextInput(attrs={'class': 'sign_in_forms'}),  # or whatever class you want to apply
        }


class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'company', 'country',
                  'address', 'zipcode', 'city', 'phone_1',
                  'website', 'firstname', 'lastname', 'post',
                  'currency', 'industry']
        
        widgets = {
            'email': forms.TextInput(attrs={'class': 'sign_up_forms'}),  # or whatever class you want to apply
            'password': forms.TextInput(attrs={'class': 'sign_up_forms'}),  # or whatever class you want to apply
        }