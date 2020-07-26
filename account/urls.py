from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.Product, name="product"),
    path('customer', views.Customer, name="customer"),
    path('', views.Home, name="Home"),
]
