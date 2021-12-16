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
        fields = ['email', 'password']


class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['phone_1', 'phone_2', 'website', 'post', 'firstname', 'lastname', 'industry',
                  'currency', 'description']

        widgets = {
            'email': forms.TextInput(attrs={'class': 'sign_up_forms'}),  # or whatever class you want to apply
            'password': forms.TextInput(attrs={'class': 'sign_up_forms'}),  # or whatever class you want to apply
        }
