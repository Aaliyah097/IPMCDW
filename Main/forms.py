from django import forms
from django.forms import widgets
from django.forms.widgets import Widget
from .models import User, Industry
from django.forms import ModelForm


class SignInForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

        widgets = {
            'email': forms.TextInput(attrs={'class': 'sign_in_forms'}),
            'password': forms.TextInput(attrs={'class': 'sign_in_forms'}),
        }


class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class EditProfileForm(ModelForm):

    #industry = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Industry.objects,
    #                                          to_field_name='name')
    class Meta:
        model = User
        fields = ['phone_1', 'phone_2', 'website', 'post', 'firstname', 'lastname', 'industry',
                  'currency', 'description', 'company', 'email', 'country', 'address', 'zipcode']

        #industry = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Industry.objects.all(), to_field_name='name')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'edit_profile_form', 'label': 'Email'}),
            'password': forms.TextInput(attrs={'class': 'edit_profile_form', 'label': 'Password'}),
            'company': forms.TextInput(attrs={'class': 'edit_profile_form', 'label': 'Company'}),
            'firstname': forms.TextInput(attrs={'class': 'edit_profile_form', 'label': 'Firstname'}),
            'lastname': forms.TextInput(attrs={'class': 'edit_profile_form', 'label': 'Lastname'}),
            'phone_1': forms.TextInput(attrs={'class': 'edit_profile_form', 'label': 'Phone number'}),
            'phone_2': forms.TextInput(attrs={'class': 'edit_profile_form', 'label': '(Add.) Phone number'}),
            'website': forms.TextInput(attrs={'class': 'edit_profile_form', 'label': 'Website'}),
            'post': forms.TextInput(attrs={'class': 'edit_profile_form', 'label': 'Post'}),
            'country': forms.Select(attrs={'class': 'edit_profile_form', 'label': 'Country'}),
            'currency': forms.Select(attrs={'class': 'edit_profile_form', 'label': 'Currency'}, choices=User.CURRENCY_VARS),
            'address': forms.TextInput(attrs={'class': 'edit_profile_form', 'label': 'Address'}),
            'zipcode': forms.TextInput(attrs={'class': 'edit_profile_form', 'label': 'Zipcode'}),
            'description': forms.Textarea(attrs={'class': 'edit_profile_form_textarea', 'label': 'Description'}),
            'industry': forms.CheckboxSelectMultiple(choices=Industry.CHOICES)
            #'industry' : forms.SelectMultiple(queryset=None)
        }


class FilterUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['country', 'industry', 'company']

        widgets = {
            'country': forms.Select(attrs={'class': 'edit_profile_form', 'label': 'Country'}),
            'industry': forms.Select(attrs={'class': 'edit_profile_form', 'label': 'Currency'}, choices=Industry.CHOICES),
            'company': forms.TextInput(attrs={'class': 'edit_profile_form', 'label': 'Company'}),
        }
