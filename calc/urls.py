from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('plans', views.plan,name='plan'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('form', views.form,name='form'),
    path('result', views.result,name='result'),
]
