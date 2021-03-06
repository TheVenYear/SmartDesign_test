from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, permissions

from products.models import Product
from products.serializers import ProductListSerializer, ProductRetrieveSerializer, ProductEditSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_queryset(self):
        params = self.request.data
        name = params.get('name', None)
        key = params.get('key', None)
        value = params.get('value', None)
        products = Product.objects.all().distinct()

        if key is not None:
            products = products.filter(params__key=key)

        if name is not None:
            products = products.filter(name=name)

        if value is not None:
            products = products.filter(params__value=value)

        return products

    def get_serializer_class(self):
        if self.action is 'list':
            return ProductListSerializer

        if self.action is 'create' or self.action is 'update':
            return ProductEditSerializer

        return ProductRetrieveSerializer

    class Meta:
        model = Product
