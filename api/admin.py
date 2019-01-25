from django.contrib import admin
from .models import Product

# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category'
    )
    list_filter = ('created_on',)
    ordering = ('created_on',)
    search_fields = ('name',)
