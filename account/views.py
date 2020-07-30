from django.shortcuts import render
from .models import *

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_oders = orders.count()
    delivred = orders.filter(status = "Delivred").count()
    pending = orders.filter(status = "pending").count()
    
    contex = {'orders':orders, 'customers': customers,'total_customers':total_customers,'total_orders':total_oders,'delivred':delivred,'pending':pending}
    return render(request,"Home.html",contex)

def products(request):
    products = Product.objects.all()
    return render(request,"product.html", {"products": products})

def customer(request):
    return render(request,"customer.html")
