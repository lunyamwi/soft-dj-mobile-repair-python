from django.urls import path
from . import views

app_name='services'

urlpatterns=[
    path('',views.service_view,name='index'),
    path('service_detail/',views.service_detail,name='service_detail'),
]