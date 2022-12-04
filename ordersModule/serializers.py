from rest_framework import serializers
from .models import Inventory, Product, Provider, User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    provider = ProviderSerializer()

    class Meta:
        model = Inventory
        fields = "__all__"
