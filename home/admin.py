from django.contrib import admin
from .models import *

admin.site.register(ProductCategory)
@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "featured",
        "is_active",
    )

    list_filter = (
        "category",
        "featured",
        "is_active",
    )

    search_fields = (
        "name",
        "subtitle",
        "description",
    )