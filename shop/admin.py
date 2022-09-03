from django.contrib import admin

from shop.models import Product, HelpdeskContact


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "release_date")
    list_filter = ("category", )


class HelpdeskContactAdmin(admin.ModelAdmin):
    list_display = ("title", "email", "text", "solved")
    list_filter = ("solved", )


admin.site.register(Product, ProductAdmin)
admin.site.register(HelpdeskContact, HelpdeskContactAdmin)
