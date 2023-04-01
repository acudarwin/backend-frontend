from rest_framework import routers
from django.urls import path, include
from .api import CategoryViewSet, ProviderViewSet, ProductViewSet, InventoryViewSet
from .views import providerTotal
router = routers.DefaultRouter()
router.register('api/warehouses/categories', CategoryViewSet, 'categories')
router.register('api/warehouses/providers', ProviderViewSet, 'providers')
router.register('api/warehouses/products', ProductViewSet, 'products')
router.register('api/warehouses/inventories', InventoryViewSet, 'inventories')

urlpatterns = [
        path('api/providers/providerTotal/', providerTotal, name='providerTotal'),
        path('', include(router.urls))
    ]
