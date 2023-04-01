from rest_framework import serializers
from .models import Category, Provider, Product, Inventory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'createdAt', 'updatedAt')
        read_only_fields = ('id', 'createdAt', 'updatedAt', )

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('id', 'name', 'address', 'phone', 'email', 'createdAt', 'updatedAt')
        read_only_fields = ('id', 'createdAt', 'updatedAt', )
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'stock', 'category', 'provider', 'createdAt', 'updatedAt')
        read_only_fields = ('id', 'createdAt', 'updatedAt', )

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'product', 'quantity', 'type', 'createdAt', 'updatedAt')
        read_only_fields = ('id', 'createdAt', 'updatedAt', )