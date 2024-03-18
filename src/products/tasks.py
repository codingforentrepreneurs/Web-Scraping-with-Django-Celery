from django.apps import apps
from celery import shared_task
import helpers


@shared_task
def scrape_product_url_task(url):
    if url is None:
        return 
    elif url == "":
        return
    ProductScrapeEvent = apps.get_model('products', 'ProductScrapeEvent')
    # open the url
    html = helpers.scrape(url=url, solve_captcha=False)
    # scrape the url
    data = helpers.extract_amazon_product_data(html)
    # save the scraped data
    ProductScrapeEvent.objects.create_scrape_event(data, url=url)
    return 


@shared_task
def scrape_products_task():
    Product = apps.get_model('products', 'Product')
    qs = Product.objects.filter(active=True)
    for obj in qs:
        url = obj.url
        scrape_product_url_task.delay(url)