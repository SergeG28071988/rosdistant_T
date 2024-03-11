from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

 