from django.db import models

# Create your models here.

from .tasks import scrape_product_url_task

class Product(models.Model):
    asin = models.CharField(max_length=120, unique=True, db_index=True)
    url = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=220, blank=True, null=True)
    current_price = models.FloatField(blank=True, null=True, default=0.00)
    timestamp =  models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now=True)
    metadata = models.JSONField(null=True, blank=True)
    active = models.BooleanField(default=True, help_text="Scrape daily?")
        


class ProductScrapeEventManager(models.Manager):
    def create_scrape_event(self, data, url=None):
        asin = data.get('asin') or None
        if asin is None:
            return None
        product, _ = Product.objects.update_or_create(
            asin=asin,
            defaults={
                "url": url,
                "title": data.get('title') or "",
                "current_price": data.get('price') or 0.00,
                "metadata": data,
            }
        )
        event = self.create(
            product=product,
            url=url,
            asin=asin,
            data=data,
        )
        return event


class ProductScrapeEvent(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='scrape_events')
    url = models.URLField(blank=True, null=True)
    data = models.JSONField(null=True, blank=True)
    asin = models.CharField(max_length=120, null=True, blank=True)
    
    objects = ProductScrapeEventManager()