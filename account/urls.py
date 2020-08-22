from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginuser, name="login"),
    path('logout/', views.logoutuser, name="logout"),
    path('register/', views.registerpage, name="register"),
    path('product/', views.products, name="product"),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('', views.home, name="Home"),
    path('createorder/<str:pk>', views.createorder, name="createorder"),
    path('updateorder/<str:pk>', views.updateorder, name="updateorder"),
    path('deleteorder/<str:pk>', views.deleteorder, name="deleteorder"),
]
