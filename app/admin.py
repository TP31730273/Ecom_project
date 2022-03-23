from django.contrib import admin

from .models import Customers


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