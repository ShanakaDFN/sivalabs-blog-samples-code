from django.urls import path

from . import views

urlpatterns = [
    path('admin/getProductUnitPrice', views.getProductUnitPrice, name='getProductUnitPrice'),
]