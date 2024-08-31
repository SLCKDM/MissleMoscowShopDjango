from django.contrib import admin

from . import models
# Register your models here.


class AttachmentStack(admin.TabularInline):
    """Класс управления и отображения медиа в админ. панели товара"""
    exclude = ['uuid']
    fields = ['uuid', 'image_tag', 'file', 'primary']
    readonly_fields = ['image_tag']
    model = models.Attachment
    show_change_link = True
    extra = 0

class AttachmentAdmin(admin.ModelAdmin):
    """Класс управления медиа в админ. панели"""
    model = models.Attachment
    fields = ['image_tag', 'file']
    readonly_fields = ['image_tag']


class CategoryAdmin(admin.ModelAdmin):
    """Класс управления категориями в админ. панели"""
    model = models.Category
    fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    """Класс управления товарами в админ. панели"""
    model = models.Product
    inlines = [
        AttachmentStack
    ]
    list_display = ["name", "article", "category", "available", "created_at", "updated_at"]
    fields = [
        "name",
        "description",
        "article",
        "barcode",
        "category",
    ]
    list_filter = [
        "category",
    ]
    search_fields = [
        "name",
        "description",
        "article",
    ]
    ordering = ["created_at"]

    def available(self, instance):
        return sum([stock.quantity for stock in instance.stocks.all()])

    # def save_formset(self, request, form, formset, change):
    #     instances = formset.save()



class StockAdmin(admin.ModelAdmin):
    """Класс управления остатками в админ. панели"""
    model = models.Stock
    # fields = []


admin.register(
    models.Attachment,
    models.Category,
    models.Product,
    models.Stock
)
admin.site.register(models.Attachment, AttachmentAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Stock, StockAdmin)
