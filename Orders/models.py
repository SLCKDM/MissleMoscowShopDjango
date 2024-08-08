import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from Catalog.models import Product
from Customers.models import Customer
# Create your models here.


class Order(models.Model):
    """Класс заказа.
    """

    class Status(models.TextChoices):
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
    name = models.IntegerField(unique=True, db_index=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        choices=Status.choices, default=Status.NEW, max_length=20
    )
    
    def __repr__(self):
        return f'<{self.__class__.__name__} {self.name}>'

    def __str__(self):
        return str(self.name)


class Position(models.Model):
    """Класс позиции заказа
    """
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.FloatField()
    payed = models.BooleanField(default=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    def __repr__(self):
        return f'<{self.__class__.__name__} {self.product.name}>'

    def __str__(self):
        return self.product.name