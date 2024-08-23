# Generated by Django 4.2.4 on 2024-08-08 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0004_alter_attachment_file_alter_attachment_product_and_more'),
        ('Customers', '0002_alter_customer_first_name_and_more'),
        ('Orders', '0002_order_updated_at_alter_order_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customers.customer', verbose_name='Покупатель'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.IntegerField(db_index=True, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'Новый'), ('in_progress', 'В процессе'), ('on_the_way', 'В пути'), ('done', 'Доставлен'), ('declined', 'Отменён'), ('returned', 'Возвращён')], default='new', max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлён'),
        ),
        migrations.AlterField(
            model_name='position',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='position',
            name='payed',
            field=models.BooleanField(default=False, verbose_name='Оплачен'),
        ),
        migrations.AlterField(
            model_name='position',
            name='price',
            field=models.FloatField(verbose_name='Стоимость (за ед.)'),
        ),
        migrations.AlterField(
            model_name='position',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Catalog.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='position',
            name='quantity',
            field=models.IntegerField(verbose_name='Кол-во'),
        ),
    ]