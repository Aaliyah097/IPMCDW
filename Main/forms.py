from django import forms
from .models import User
from django.forms import ModelForm


class SignInForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form_wrapper'}),  # or whatever class you want to apply
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
