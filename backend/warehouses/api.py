from .models import Category, Provider, Product, Inventory
from rest_framework import viewsets, permissions
from .serializers import CategorySerializer, ProviderSerializer, ProductSerializer, InventorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProviderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = InventorySerializer
