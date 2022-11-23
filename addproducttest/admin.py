from django.contrib import admin

from django.db import models

from addproducttest.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Product, ProductAdmin)


