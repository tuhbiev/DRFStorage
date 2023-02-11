from django.contrib import admin
from .models import Category, Price, Product


@admin.register(Product)
class AdminPanel(admin.ModelAdmin):
    list_display = ('name', 'barcode', 'category', 'pr_price',  'count', 'data_update')
    list_filter = ('name', 'category')
    search_fields = ('name', 'barcode', 'category', 'pr_price')


admin.site.register(Price)
admin.site.register(Category)


