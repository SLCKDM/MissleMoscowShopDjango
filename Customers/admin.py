from django.contrib import admin

from . import models 

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    model = models.Customer
    fields = ['id', 'first_name', 'last_name', 'username']
    readonly_fields = ['image_tag']
    
admin.site.register(models.Customer, CustomerAdmin)
    