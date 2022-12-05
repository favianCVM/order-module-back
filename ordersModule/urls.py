from django.contrib import admin
from django.urls import path

# from .views import getProvidersAndProducts, GetProvidersAndProductsEndPoint
from .views import (
    GetProductsEndPoint,
    GetUsersEndPoint,
    GetProvidersEndPoint,
    GetAllOrdersEndPoint,
    createOrderEndPoint,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("get-products", GetProductsEndPoint, basename="products")
router.register("get-users", GetUsersEndPoint, basename="users")
router.register("get-providers", GetProvidersEndPoint, basename="providers")
router.register("get-orders", GetAllOrdersEndPoint, basename="orders")

urlpatterns = router.urls

urlpatterns += [
    path("admin/", admin.site.urls),
    path("create-order", createOrderEndPoint),
]
