from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'id', 'category', 'created_on')
        read_only_fields = ('created_on', 'id')
