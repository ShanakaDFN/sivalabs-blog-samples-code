from django.shortcuts import render
from data.models import Product
from django.http import JsonResponse


def getProductUnitPrice(request):
    if request.method == "GET":
        product_id = request.GET['product_id']
        product = Product.objects.get(pk=product_id)
        return JsonResponse({"unit_price":product.unit_price})

