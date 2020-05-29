from django.contrib import admin
from django.urls import path, include
from my_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_search', views.new_search, name='new_search'),
    path('largest_price', views.largest_price, name='largest_price'),
]
