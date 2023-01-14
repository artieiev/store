from products.models import Product, ProductCategory
from rest_framework import serializers


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
