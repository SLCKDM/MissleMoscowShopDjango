from django.contrib import admin

from . import models 

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    model = models.Customer
    fields = ['id', 'first_name', 'last_name', 'username']
    
admin.site.register(models.Customer, CustomerAdmin)
    