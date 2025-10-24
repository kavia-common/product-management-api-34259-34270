from django.urls import path
from .views import (
    health,
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
    total_inventory_balance,
)

urlpatterns = [
    path('health/', health, name='Health'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/total-balance/', total_inventory_balance, name='products-total-balance'),
    path('products/<int:id>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
]
