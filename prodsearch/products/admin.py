from django.contrib import admin

# Register your models here.
from .models import Product, ProductImage, ProductCategory


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'position']

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'name']


admin.site.register(Product)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
