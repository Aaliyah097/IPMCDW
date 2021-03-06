from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.enter_page, name='enter_page'),
    path('recovery/', views.recovery_page, name='recovery_page'),
    path('sign_in/', views.sign_in_page, name='sign_in_page'),
    path('sign_up/', views.sign_up_page, name='sign_up_page'),
    path('lk/<int:pk>', views.lk, name='lk'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('lk/edit_profile/<int:pk>', views.edit_profile_page, name='edit_profile_page'),
    path('companies/', views.companies, name='companies'),
    path('change_lang/', views.change_lang, name='change_lang'),
]

urlpatterns = format_suffix_patterns(urlpatterns)