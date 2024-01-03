from django.contrib import admin

from Product.models import Product


# Register your models here.

# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)  # Добавление фильтрации по категории
    search_fields = ('name', 'description',)  # Добавление возможности поиска по названию и описанию
