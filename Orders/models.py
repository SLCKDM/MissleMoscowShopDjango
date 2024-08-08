import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from Catalog.models import Product
from Customers.models import Customer
# Create your models here.


class Order(models.Model):
    """Класс заказа.
    
    Args:
        id (int): идентификатор заказа;
        name (int): название заказа;
        customer (int): покупатель;
        created_at (datetime): дата и время создания заказа;
        updated_at (datetime): дата и время обновления заказа;
        status (str): статус заказа;
    """

    class Status(models.TextChoices):
        """Статус заказа.
        
        Args:
            NEW: новый;
            IN_PROGRESS: в процессе
            ON_THE_WAY: в пути
            DONE: доставлен
            DECLINED: отменен
            RETURNED: возвращен
        """
        NEW = "new", _('Новый')
        IN_PROGRESS = "in_progress", _('В процессе')
        ON_THE_WAY = "on_the_way", _('В пути')
        DONE = "done", _('Доставлен')
        DECLINED = "declined", _('Отменён')
        RETURNED = "returned", _('Возвращён')
        
        # @classmethod
        # def as_set(cls):
        #     return {
        #         cls.NEW,
        #         cls.IN_PROGRESS,
        #         cls.ON_THE_WAY,
        #         cls.DONE,
        #         cls.DECLINED,
        #         cls.RETURNED,
        #     }
    
    
    id = models.IntegerField(
        primary_key=True, unique=True, editable=False, auto_created=True
    )
    name = models.IntegerField(
        unique=True, db_index=True, verbose_name="Название"
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name="Покупатель"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлён")
    status = models.CharField(
        choices=Status.choices, default=Status.NEW, max_length=20,
        verbose_name="Статус"
    )
    
    def __repr__(self):
        return f'<{self.__class__.__name__} {self.name}>'

    def __str__(self):
        return str(self.name)


class Position(models.Model):
    """Класс позиции заказа.
    
    Args:
        id (uuid): идентификатор позиции;
        quantity (int): количество товара;
        product (uuid): товар;
        price (float): цена позиции (за единицу);
        payed (bool): оплачен;
        order (int): связанный заказ;
    """
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    quantity = models.IntegerField(verbose_name="Кол-во")
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, verbose_name="Товар"
    )
    price = models.FloatField(verbose_name="Стоимость (за ед.)")
    payed = models.BooleanField(default=False, verbose_name="Оплачен")
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="Заказ"
    )
    
    def __repr__(self):
        return f'<{self.__class__.__name__} {self.product.name}>'

    def __str__(self):
        return self.product.name