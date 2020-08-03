from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.products, name="product"),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('', views.home, name="Home"),
    path('createorder/<str:pk>', views.createorder, name="createorder"),
    path('updateorder/<str:pk>', views.updateorder, name="updateorder"),
    path('deleteorder/<str:pk>', views.deleteorder, name="deleteorder"),
]
