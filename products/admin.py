from django.contrib import admin

from products.models import Product, Parameter


class ParameterInline(admin.TabularInline):
    model = Parameter
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    inlines = [
        ParameterInline,
    ]

