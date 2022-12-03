from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Inventory
from rest_framework import status

def getProvidersAndProducts(request):
    data = list(Inventory.objects.all().values())

    print(data)
    return JsonResponse(data, safe=False, status=status.HTTP_200_OK)


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
