from django.contrib import admin
from .models import Category, Subcategory


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['category_name']
    prepopulated_fields = {'slug': ['category_name']}
    list_display = ['category_name', 'slug']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [ 'sub_category_name', 'category_name']
    search_fields = ['sub_category_name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubCategoryAdmin)
