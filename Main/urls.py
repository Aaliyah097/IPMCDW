from django.urls import path
from . import views


urlpatterns = [
    path('', views.enter_page, name='enter_page'),
    path('recovery/', views.recovery_page, name='recovery_page'),
    path('lk/', views.lk_page, name='lk_page'),
    path('all_company/', views.all_company_page, name='all_company_page')

]