from django.db import models

# Usuarios
class User(models.Model):
    class Meta:
        db_table = "users"

    def __str__(self):
        return self.first_name

    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)


# Categorias de productos
class ProductCategory(models.Model):
    class Meta:
        db_table = "product_categories"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=500)


# Proveedores
class Provider(models.Model):
    class Meta:
        db_table = "providers"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=500)


# Ordenes
class Order(models.Model):
    class Meta:
        db_table = "orders"

    date = models.DateField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)


# Productos
class Product(models.Model):
    class Meta:
        db_table = "products"

    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)


# --------------------------------------------------- tablas puente ---------------------------------


class ProductPerOrder(models.Model):
    class Meta:
        db_table = "products_per_orders"

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()


class Inventory(models.Model):
    class Meta:
        db_table = "inventories"

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
