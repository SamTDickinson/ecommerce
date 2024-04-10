from django.contrib import admin

from .models import Product, ProductAddOn


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'rrp', 'stock', 'category', 'sub_category', 'is_available', 'created_date']
    prepopulated_fields = {'slug': ['product_name']}


class ProductAddonAdmin(admin.ModelAdmin):
    list_display = ['product_addon_name', 'product_name']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAddOn, ProductAddonAdmin)
