from typing import Any
from django.db import models
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError

import uuid

# Create your models here.


class Category(models.Model):
    """Категория товара.

    Args:
        uuid (uuid): идентифкатор категории;
        name (str): название категории; 
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=200)

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.name}>'

    def __str__(self):
        return self.name


class Attachment(models.Model):
    """Медиа товаров.
    
    Args:
        uuid (uuid): идентификатор;
        file (str?): изображение;
        product (uuid): идентификатор связанного товара;
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    file = models.ImageField(upload_to="attachments/")
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='attachments')

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.uuid}>'

    def __str__(self):
        return f'<{self.__class__.__name__} {self.uuid}>'

    def image_tag(self):
        if not self.file:
            return ''
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.file))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class Product(models.Model):
    """Товары
    
    Args:
        uuid (uuid): идентификатор;
        name (str): название;
        description (str): описание;
        article (str): артикул;
        barcode (str): баркод;
        category (int): категория;
        created_at (datetime): дата и время создания;
        updated_at (datetime): дата и время обновления;
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, null=True, blank=True)
    article = models.CharField(max_length=200, blank=True, null=True)
    barcode = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.name}>'

    def __str__(self):
        return f'<{self.__class__.__name__} {self.name}>'


class Stock(models.Model):
    """Остаток товара.
    
    Args:
        product (uuid): идентификатор товара;
        quantity (int): количество товара;
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stocks')
    quantity = models.IntegerField()

    def is_available(self) -> bool:
        """Проверка доступности (кол-во > 0) товара."""
        return self.quantity > 0

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.product} - {self.quantity}>'

    def __str__(self):
        return f'<{self.__class__.__name__} {self.product} - {self.quantity}>'

    def decrease(self, q: int):
        """Уменьшить количество товара на :q:.

        Args:
            q (int): вычитаемое.

        Raises:
            ValidationError: Если вычитаемое менее или равно 0.
        """
        if self.quantity <= 0:
            raise ValidationError('There is no fucking way to decrease product amount lesser than / equal ZERO')
        self.quantity = self.quantity - abs(q)
        self.save()

    def increase(self, q: int):
        """Увеличить количество товара на :q:.

        Args:
            q (int): слагаемое.

        Raises:
            ValidationError: Если кол-во менее или равно 0.
        """
        if q <= 0:
            raise ValidationError('Why wont you use `.decrease(q) method?`')
        self.quantity = self.quantity - abs(q)
        self.save()