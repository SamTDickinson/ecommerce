from django.contrib import admin

from .models import Product, ProductAddOn, Variation


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'rrp', 'our_price', 'stock', 'category', 'sub_category', 'is_available', 'created_date']
    prepopulated_fields = {'slug': ['product_name']}


class ProductAddonAdmin(admin.ModelAdmin):
    list_display = ['product_addon_name', 'product_name']


class VariationAdmin(admin.ModelAdmin):
    list_display = ['product', 'variation_category', 'variation_value', 'is_active']
    list_editable = ['is_active']
    list_filter = ['product', 'variation_category', 'variation_value']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAddOn, ProductAddonAdmin)
admin.site.register(Variation, VariationAdmin)
