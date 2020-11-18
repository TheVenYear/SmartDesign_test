from django.shortcuts import render
from rest_framework import viewsets, permissions

from products.models import Product
from products.serializers import ProductSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    class Meta:
        model = Product
