from django.urls import path
from . import views

app_name='blog'

urlpatterns=[
    path('',views.article_view,name='blog_list'),
    path('blog_detail/',views.article_detail,name='blog_detail'),
]