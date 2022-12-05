from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Product, User, Provider, Order
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import (
    ProductSerializer,
    UserSerializer,
    ProviderSerializer,
    CreateOrderSerializer,
    CreateProductPerOrderSerializer,
    OrderSerializer,
)
from rest_framework import viewsets, status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
def createOrderEndPoint(request):
    print(request.data)

    # ACTUALIZAR PRODUCTOS
    for updatedProduct in request.data["products"]:
        product = Product.objects.get(pk=updatedProduct["id"])
        product.quantity = product.quantity - updatedProduct["quantity"]
        product.save()

    # GUARDAR ORDEN
    orderSerializer = CreateOrderSerializer(
        data={
            "date": request.data["date"],
            "provider": request.data["provider_id"],
            "user": request.data["user_id"],
        }
    )

    orderId = None

    if orderSerializer.is_valid():
        order = orderSerializer.save()
        orderId = order.id
    else:
        return Response(orderSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ORDENES POR PRODUCTOS
    for product in request.data["products"]:
        productPerOrderSerializer = CreateProductPerOrderSerializer(
            data={
                "order": orderId,
                "product": product["id"],
                "quantity": product["quantity"],
            }
        )
        if productPerOrderSerializer.is_valid():
            productPerOrderSerializer.save()
        else:
            return Response(orderSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_201_CREATED)

class GetAllOrdersEndPoint(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class GetProvidersEndPoint(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class GetUsersEndPoint(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    queryset = User.objects.all()


class GetProductsEndPoint(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    queryset = Product.objects.all()

    # def get_queryset(self):
    #     return Product.objects.raw(
    #         "SELECT * FROM products INNER JOIN product_categories ON products.product_category_id = product_categories.id"
    #     )


# class GetProvidersAndProductsEndPoint(viewsets.ModelViewSet):
#     # model = Inventory
#     # permission_classes = [AllowAny]
#     serializer_class = InventorySerializer

#     def get_queryset(self):
#         return Inventory.objects.raw(
#             "SELECT * FROM inventories LEFT JOIN products ON  products.id = inventories.product_id LEFT JOIN providers ON providers.id = inventories.provider_id"
#         )

#     # def list(self, request):

#     #     serializer = InventorySerializer()
#     #     return Response(serializer.data)


def getProvidersAndProducts(request):
    # data = list(Inventory.objects.all().select_related("product").values())
    # data = list(
    #     Inventory.objects.raw(
    #         "SELECT * FROM inventories INNER JOIN products WHERE inventories.product_id = products.id"
    #     )
    # )

    data = list(
        Inventory.objects.all()
        .values()
        .annotate(product="product_id", provider="provider_id")
    )

    # print(data.query)
    print(data)

    # return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
    return HttpResponse(data, status=status.HTTP_200_OK)
