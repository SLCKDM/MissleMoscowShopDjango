# Generated by Django 4.2.4 on 2024-08-08 18:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Customers', '0001_initial'),
        ('Catalog', '0002_product_created_at_product_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.IntegerField(db_index=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('new', 'Новый'), ('in_progress', 'В процессе'), ('on_the_way', 'В пути'), ('done', 'Доставлен'), ('declined', 'Отменён'), ('returned', 'Возвращён')], default='new', max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customers.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('payed', models.BooleanField(default=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Catalog.product')),
            ],
        ),
    ]
