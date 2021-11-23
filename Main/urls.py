from django.urls import path
from . import views


urlpatterns = [
    path('', views.enter_page, name='enter_page'),
    path('recovery/', views.recovery_page, name='recovery_page'),

]