from django.contrib import admin
from django.urls import path
from .views import getProvidersAndProducts, GetProvidersAndProductsEndPoint
from rest_framework import routers

router = routers.DefaultRouter()
router.register(
    "get-provider-inventory", GetProvidersAndProductsEndPoint, basename="inventory"
)

urlpatterns = router.urls

urlpatterns += [
    path("admin/", admin.site.urls),
    # path("get-provider-inventory", getProvidersAndProducts),
    # path("get-provider-inventory", InventoryEndPoint.as_view()),
]
