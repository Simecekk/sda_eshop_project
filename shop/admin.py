from django.contrib import admin

from shop.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "release_date")
    list_filter = ("category", )


admin.site.register(Product, ProductAdmin)
