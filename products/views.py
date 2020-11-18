from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, permissions

from products.models import Product
from products.serializers import ProductListSerializer, ProductRetrieveSerializer, ProductEditSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_queryset(self):
        qp = self.request.query_params

        if 'value' in qp.keys() and 'key' in qp.keys():
            values = Product.objects.filter(params__key=qp['key'], params__value=qp['value'])
            return values

        if 'key' in qp.keys():
            return Product.objects.filter(params__key=qp['key'])

        if 'value' in qp.values():
            return Product.objects.filter(params__value=qp['value'])

        return Product.objects.all()

    def get_serializer_class(self):
        if self.action is 'list':
            return ProductListSerializer

        if self.action is 'create' or self.action is 'update':
            return ProductEditSerializer

        return ProductRetrieveSerializer

    class Meta:
        model = Product
