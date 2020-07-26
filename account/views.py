from django.shortcuts import render

def Home(request):
    return render(request,"Home.html")
def Product(request):
    return render(request,"product.html")
def Customer(request):
    return render(request,"customer.html")
