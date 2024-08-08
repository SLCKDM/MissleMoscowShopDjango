from django.contrib import admin

from Orders.models import Position, Order

# Register your models here.

class PositionStack(admin.StackedInline):
    """Класс отображения позиций в заказе в админ. панели"""
    exclude = ['id']
    model = Position
    fields = ['id', 'quantity', 'price', 'payed']
    readonly_fields = ['quantity', 'price', 'payed']
    show_change_link = False
    extra = 0

class PositionAdmin(admin.ModelAdmin):
    """Класс управления позициями в админ. панели"""
    model = Position
    list_display = ["product", "quantity", "price", "payed", "order"]
    list_filter = ["product", "price", "payed", "quantity"]
    search_fields = ["order"]
    # inlines = ["order"]


class OrderAdmin(admin.ModelAdmin):
    """Класс управления заказами в админ. панели"""
    model = Order
    list_display = ["id", "name", "status", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["name"]
    inlines = [PositionStack]
    
    
admin.site.register(Position, PositionAdmin)
admin.site.register(Order, OrderAdmin)
