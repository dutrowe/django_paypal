from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola, name= 'inicio'),
    path('pago/', views.pago, name= 'pago'),
]