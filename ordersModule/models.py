from django.db import models

# Categorias de productos
class ProductCategory(models.Model):
    class Meta:
        db_table = "product_categories"

    name = models.CharField(max_length=500)


# Proveedores
class Provider(models.Model):
    class Meta:
        db_table = "providers"

    name = models.CharField(max_length=500)


# Ordenes
class Order(models.Model):
    class Meta:
        db_table = "orders"

    date = models.DateField()
    providerId = models.ForeignKey(Provider, on_delete=models.CASCADE)


# Productos
class Product(models.Model):
    class Meta:
        db_table = "products"

    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    quantity = models.IntegerField()
    productCategoryId = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)


# Usuarios
class User(models.Model):
    class Meta:
        db_table = "users"

    firstName = models.CharField(max_length=500)
    lastName = models.CharField(max_length=500)


# --------------------------------------------------- tablas puente ---------------------------------


class ProductPerOrder(models.Model):
    class Meta:
        db_table = "products_per_orders"

    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
