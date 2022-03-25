from django.contrib import admin

from .models import Customers, Sellers, Category, Product


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'last_login',
        'email',
        'username',
        'password',
        'image',
    )
    list_filter = ('last_login',)


@admin.register(Sellers)
class SellersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'last_login',
        'email',
        'username',
        'password',
        'Shop_name',
        'image',
    )
    list_filter = ('last_login',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product_name',
        'product_description',
        'product_price',
        'product_image',
        'product_category',
        'seller',
    )
    list_filter = ('product_category', 'seller')