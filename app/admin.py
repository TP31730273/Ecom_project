from django.contrib import admin

from .models import UserAccount, Customers, Sellers, Category, Product


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'email',
        'username',
        'image',
        'is_staff',
        'is_active',
    )
    list_filter = ('last_login', 'is_superuser', 'is_staff', 'is_active')
    raw_id_fields = ('groups', 'user_permissions')


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'email',
        'username',
        'image',
        'is_staff',
        'is_active',
    )
    list_filter = ('last_login', 'is_superuser', 'is_staff', 'is_active')


@admin.register(Sellers)
class SellersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'email',
        'username',
        'image',
        'is_staff',
        'is_active',
        'shop_name',
        'is_seller',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'is_seller',
    )


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
        'is_active',
        'date_modified',
        'date_created',
    )
    list_filter = (
        'product_category',
        'seller',
        'is_active',
        'date_modified',
        'date_created',
    )