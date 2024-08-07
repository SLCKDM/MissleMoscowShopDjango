from django.contrib import admin

from Orders.models import Position, Order

# Register your models here.
class PositionAdmin(admin.ModelAdmin):
    model = Position
    list_display = ["product", "quantity", "price", "payed", "order"]
    list_filter = ["product", "price", "payed", "quantity"]
    # inlines = ["order"]


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ["id", "name", "status", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["name"]
    # inlines = []
    
    
admin.site.register(Position, PositionAdmin)
admin.site.register(Order, OrderAdmin)
