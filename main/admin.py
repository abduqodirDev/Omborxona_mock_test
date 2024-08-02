from django.contrib import admin
from .models import Product, Material, Product_Material


class Product_Material_Table(admin.TabularInline):
    model = Product_Material
    extra = 1


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price')


@admin.register(Product_Material)
class MaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (Product_Material_Table, )
