from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    category_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('store:products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name


class Subcategory(models.Model):
    category_name = models.ForeignKey(Category, related_name='category', null=True, blank=True, on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    category_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.sub_category_name
