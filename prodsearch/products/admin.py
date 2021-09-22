from django.contrib import admin

# Register your models here.
from .models import Product, ProductImage, ProductCategory


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'position']


admin.site.register(Product)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductCategory)