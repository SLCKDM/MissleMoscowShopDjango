# Generated by Django 4.2.4 on 2024-08-08 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0002_product_created_at_product_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]
