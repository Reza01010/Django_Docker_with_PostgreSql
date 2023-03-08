from django.contrib import admin

from .models import Product


# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'datetime_created', 'active',]

