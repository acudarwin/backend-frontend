from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Provider, Product, Inventory
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def providerTotal(request):
    try:
        total = Provider.objects.all().count()
        return JsonResponse({
            "providers": total
        },
        safe=False,
        status=200
        )
    except Product.DoesNotExist:
        return JsonResponse({
            "message": "No providers found"
            },status=400)