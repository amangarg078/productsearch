from django.db import models

from .managers import ProductManager
# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.IntegerField()
    url = models.URLField()
    title = models.CharField(max_length=512)
    description = models.TextField()
    source = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    price = models.FloatField()
    discount = models.FloatField(null=True, blank=True)
    currency_code = models.CharField(max_length=3)
    categories = models.ManyToManyField(ProductCategory, blank=True)
    colour = models.CharField(max_length=20, null=True, blank=True)
    imgs_src = models.URLField()
    stock = models.IntegerField(default=1)

    objects = ProductManager()

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.URLField()
    checksum = models.CharField(max_length=100)
    path = models.CharField(max_length=512)
    position = models.CharField(max_length=20)
