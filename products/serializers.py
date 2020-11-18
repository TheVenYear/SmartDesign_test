from rest_framework import serializers

from products.models import Product, Parameter


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        exclude = ('product',)


class ProductSerializer(serializers.ModelSerializer):
    params = ParameterSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'params')
