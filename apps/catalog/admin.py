from django.contrib import admin
from apps.catalog.models import Category, Product, Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


class ProductCategoryInline(admin.TabularInline):
    model = Product.categories.through
    extra = 1


class ImageInline(admin.TabularInline):
    model = Image
    fields = ['product', 'image_tag', 'image', 'is_main']
    readonly_fields = ['image_tag']
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'quantity', 'price']
    list_display_links = ['id', 'name']
    fields = ['name', 'description', 'quantity', 'price']
    inlines = [ProductCategoryInline, ImageInline]

