# Generated by Django 4.1.3 on 2022-12-03 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordersModule', '0002_remove_product_quantity_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='productId',
            field=models.ForeignKey(db_column='productId', on_delete=django.db.models.deletion.CASCADE, to='ordersModule.product'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='providerId',
            field=models.ForeignKey(db_column='providerId', on_delete=django.db.models.deletion.CASCADE, to='ordersModule.provider'),
        ),
        migrations.AlterField(
            model_name='order',
            name='providerId',
            field=models.ForeignKey(db_column='providerId', on_delete=django.db.models.deletion.CASCADE, to='ordersModule.provider'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productCategoryId',
            field=models.ForeignKey(db_column='productCategoryId', on_delete=django.db.models.deletion.CASCADE, to='ordersModule.productcategory'),
        ),
        migrations.AlterField(
            model_name='productperorder',
            name='orderId',
            field=models.ForeignKey(db_column='orderId', on_delete=django.db.models.deletion.CASCADE, to='ordersModule.order'),
        ),
        migrations.AlterField(
            model_name='productperorder',
            name='productId',
            field=models.ForeignKey(db_column='productId', on_delete=django.db.models.deletion.CASCADE, to='ordersModule.product'),
        ),
    ]
