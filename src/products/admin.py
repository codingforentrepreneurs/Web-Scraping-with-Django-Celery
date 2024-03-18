from django.contrib import admin

# Register your models here.

from .models import Product, ProductScrapeEvent


admin.site.register(Product)

admin.site.register(ProductScrapeEvent)