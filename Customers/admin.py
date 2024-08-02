from django.contrib import admin

from models import Customer 

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    fields = ['id', 'first_name', 'last_name', 'username']
    readonly_fields = ['image_tag']
    
admin.site.register(Customer, CustomerAdmin)
    