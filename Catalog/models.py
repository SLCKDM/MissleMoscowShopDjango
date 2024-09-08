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
    name = models.CharField(max_length=200, verbose_name="Название")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.name}>'

    def __str__(self):
        return str(self.name)


class Attachment(models.Model):
    """Медиа товаров.

    Args:
        uuid (uuid): идентификатор;
        file (str?): изображение;
        product (uuid): идентификатор связанного товара;
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    # file = models.ImageField(upload_to="attachments/", verbose_name="Файл")
    file = models.FileField(verbose_name="Файл")
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name="attachments",
        verbose_name="Товар"
    )
    primary = models.BooleanField(verbose_name='Главная', null=True, blank=True)

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.uuid}>'

    def __str__(self):
        return f'<{self.__class__.__name__} {self.uuid}>'

    def image_tag(self):
        """Получить тег изображения."""
        if not self.file:
            return ''
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.file.url))

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
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(
        max_length=2000, null=True, blank=True, verbose_name="Описание"
    )
    article = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Артикул")
    barcode = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Баркод")
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL,
        related_name='products', verbose_name="Категория"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлён")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.name}>'

    def __str__(self):
        return f'<{self.__class__.__name__} {self.name}>'

    def primary_image(self):
        """Получить главное изображение.
        Ищет инстанс ``Attachment`` у которого значение
        атрибута ``primary==True``.
        - Если несколько - возвращет первый;
        - Если ни одного ``primary==True``, но есть ``Attachments`` - возвращает первый из них;
        - Если ``Attachments`` остсутствуют - None.
        """
        primaries = self.attachments.filter(primary=True)
        if primaries:
            primary = primaries[0]
        else:
            primary = self.attachments.first()
        return primary


class Stock(models.Model):
    """Остаток товара.

    Args:
        product (uuid): идентификатор товара;
        quantity (int): количество товара;
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='stocks', verbose_name="Товар"
    )
    quantity = models.IntegerField(verbose_name="Кол-во")

    class Meta:
        verbose_name = "Остаток"
        verbose_name_plural = "Остатки"

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
