from rest_framework import serializers, fields
from .models import Product, Provider, User, ProductCategory, Order, ProductPerOrder


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    product_category = ProductCategorySerializer()

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


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    provider = ProviderSerializer()

    class Meta:
        model = Order
        fields = "__all__"


class ProductPerOrderSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    product = ProductSerializer()

    class Meta:
        model = ProductPerOrder
        fields = "__all__"

# -------------------------------------------------------------------------------------
class CreateOrderSerializer(serializers.ModelSerializer):
    # provider = ProviderSerializer()
    # user = UserSerializer()

    date = fields.DateField(input_formats=["%Y-%m-%dT%H:%M:%S.%fZ"])

    class Meta:
        model = Order
        fields = "__all__"


class CreateProductPerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPerOrder
        fields = "__all__"


class GetOrderProducts(serializers.ModelSerializer):
    product = ProductSerializer()
    order = OrderSerializer()
    class Meta:
        model = ProductPerOrder
        fields = "__all__"
