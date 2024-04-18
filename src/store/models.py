from django.db import models
from django.urls import reverse

from category.models import Category, Subcategory
from .variation_categories import get_variation_category_choice
from .variation_manager import VariationManager


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=5000)
    rrp = models.FloatField()
    our_price = models.FloatField()
    fitted_price = models.FloatField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('store:product_detail', args=[self.category.slug, self.slug])


class ProductAddOn(models.Model):
    product_addon_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=5000)
    product_name = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    rrp = models.FloatField()

    def __str__(self):
        return self.product_addon_name


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=get_variation_category_choice)
    variation_value = models.CharField(max_length=100)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return {'variation_value': self.variation_value, 'price': self.price}
