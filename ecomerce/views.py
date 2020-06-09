from django.shortcuts import render

# Create your views here.
def ecomerce_view(request):
    return render(request,'shop.html')

def cart_view(request):
    return render(request,'cart.html')

def checkout_view(request):
    return render(request,'cart.html')