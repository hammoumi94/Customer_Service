from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.products, name="product"),
    path('customer', views.customer, name="customer"),
    path('', views.home, name="Home"),
]
