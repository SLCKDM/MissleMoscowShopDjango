# Generated by Django 4.2.4 on 2024-08-23 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0004_alter_attachment_file_alter_attachment_product_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'verbose_name': 'Фото', 'verbose_name_plural': 'Фото'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': 'Остаток', 'verbose_name_plural': 'Остатки'},
        ),
    ]