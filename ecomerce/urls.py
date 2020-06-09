from django.urls import path
from . import views

app_name='ecomerce'

urlpatterns=[
    path('',views.ecomerce_view,name='index'),
    path('cart/',views.cart_view,name='cart'),
    path('checkout/',views.checkout_view,name='checkout'),
]