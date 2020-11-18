from rest_framework import serializers

from products.models import Product, Parameter


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        exclude = ('product',)


class ParameterEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        exclude = ('product', 'id')


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')


class ProductRetrieveSerializer(serializers.ModelSerializer):
    params = ParameterSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductEditSerializer(serializers.ModelSerializer):
    params = ParameterEditSerializer(many=True, required=False)

    def create(self, validated_data):
        params = validated_data.pop('params')
        product = Product.objects.create(**validated_data)
        parameters = []
        for item in params:
            parameters.append(Parameter.objects.create(**item, product_id=product.id))
        return product

    def update(self, instance, validated_data):
        params = validated_data.pop('params')
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        parameters = []

        instance.params.all().delete()

        for item in params:
            parameters.append(Parameter.objects.create(**item, product_id=instance.id))

        return instance

    class Meta:
        model = Product
        fields = '__all__'
