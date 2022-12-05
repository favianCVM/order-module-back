from django.contrib import admin
from django.urls import path

from .views import (
    GetProductsEndPoint,
    GetUsersEndPoint,
    GetProvidersEndPoint,
    GetAllOrdersEndPoint,
    createOrderEndPoint,
    GetOrderProductsEndPoint,
    GetOrderDetailsEndPoint,
    approveOrderStatusEndPoint,
    cancelOrderStatusEndPoint
    # getOrderDetailsEndPoint,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("get-products", GetProductsEndPoint, basename="products")
router.register("get-users", GetUsersEndPoint, basename="users")
router.register("get-providers", GetProvidersEndPoint, basename="providers")
router.register("get-orders", GetAllOrdersEndPoint, basename="orders")
router.register("get-orders", GetAllOrdersEndPoint, basename="orders")
router.register("order-products", GetOrderProductsEndPoint, basename="order-products")
router.register("order-details", GetOrderDetailsEndPoint, basename="order-details")

urlpatterns = router.urls

urlpatterns += [
    path("admin/", admin.site.urls),
    path("create-order", createOrderEndPoint),
    path("approve-order", approveOrderStatusEndPoint),
    path("cancel-order", cancelOrderStatusEndPoint),
]
