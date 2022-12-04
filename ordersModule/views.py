from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Inventory, Product
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from .serializers import InventorySerializer
from rest_framework import viewsets, status


# @api_view(["GET", "POST", "DELETE"])
class InventoryEndPoint(viewsets.ModelViewSet):
    # model = Inventory
    serializer_class = InventorySerializer

    def get_queryset(self):
        return Inventory.objects.raw(
            "SELECT * FROM inventories INNER JOIN products WHERE inventories.product_id = products.id"
        )

    # def list(self, request):

    #     serializer = InventorySerializer()
    #     return Response(serializer.data)


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


# EJEMPLO DE POST CON DATA EN UN FORMULARIO Y MANEJO DE VALIDACION DE CAMPOS
# def modelformData(request):
#     form =studentForm()
#     if request.method == 'POST':
#         form =studentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('saved to database......')
#         else:
#             return HttpResponse(form.errors)
#     return render(request, 'myNewapp/model.html', {'form': form})
