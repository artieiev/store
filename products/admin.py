from django.contrib import admin
from .models import ProductCategory, Product, Basket

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    readonly_fields = ('short_description',)
    ordering = ('name',)
    search_fields = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
