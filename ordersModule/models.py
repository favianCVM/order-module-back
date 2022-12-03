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
    providerId = models.ForeignKey(
        Provider, on_delete=models.CASCADE, db_column="providerId"
    )


# Productos
class Product(models.Model):
    class Meta:
        db_table = "products"

    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    productCategoryId = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, db_column="productCategoryId"
    )


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

    productId = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column="productId"
    )
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE, db_column="orderId")
    amount = models.IntegerField()


class Inventory(models.Model):
    class Meta:
        db_table = "inventories"

    providerId = models.ForeignKey(
        Provider, on_delete=models.CASCADE, db_column="providerId"
    )
    productId = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column="productId"
    )
    quantity = models.IntegerField()
