# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock_list, name='stock_list'),
    path('add_stock/', views.add_stock, name='add_stock'),
]
