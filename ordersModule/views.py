from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Product, User, Provider, Order, ProductPerOrder
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import (
    ProductSerializer,
    UserSerializer,
    ProviderSerializer,
    CreateOrderSerializer,
    CreateProductPerOrderSerializer,
    OrderSerializer,
    GetOrderProducts,
)
from rest_framework import viewsets, status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


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


@csrf_exempt
@api_view(["PUT"])
def approveOrderStatusEndPoint(request):
    print(request.data)

    id = request.data["id"]

    try:
        order = Order.objects.get(pk=id)
        order.status = "APPROVED"
        order.save()
    except Exception:
        return Response(exception=Exception, status=status.HTTP_400_BAD_REQUEST)
    finally:
        return Response(status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(["PUT"])
def cancelOrderStatusEndPoint(request):
    print(request.data)

    id = request.data["id"]

    try:
        order = Order.objects.get(pk=id)
        order.status = "CANCELED"
        order.save()
    except Exception:
        return Response(exception=Exception, status=status.HTTP_400_BAD_REQUEST)
    finally:
        return Response(status=status.HTTP_201_CREATED)


class GetOrderProductsEndPoint(viewsets.ModelViewSet):
    queryset = ProductPerOrder.objects.all()
    serializer_class = GetOrderProducts
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["order"]


class GetOrderDetailsEndPoint(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        id = self.request.query_params.get("id")
        queryset = Order.objects.all()
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset


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
