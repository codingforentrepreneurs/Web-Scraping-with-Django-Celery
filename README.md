# Web Scraping on a Schedule with Django & Celery
Learn how to schedule regular web scraping, save the data, and more with Django &amp; Celery.

Topics:

- Django
- Celery
- Selenium
- Scraped Data to Database via Django
- Reliable Web Scraping with Selenium + Bright Data

References:
- [Celery + Redis + Django configuration guide](https://www.codingforentrepreneurs.com/blog/celery-redis-django/)
- Django + Celery Redis [blank project code](https://github.com/codingforentrepreneurs/Django-Celery-Redis)
- Django + Jupyter Setup Module [short + code](https://www.codingforentrepreneurs.com/shorts/django-setup-for-use-in-jupyter-notebooks/)

Requirements:
- Django experience such as Try Django (on [YouTube](https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL) or on [CFE](https://www.codingforentrepreneurs.com/topics/try-django/)) or [Your First Django Project](https://www.codingforentrepreneurs.com/courses/your-first-django-project/).
- Redis Instance
  - Setup Redis on Windows [blog post](https://www.codingforentrepreneurs.com/blog/redis-on-windows/)
  - Setup Redis on MacOS or Linux [blog post](https://www.codingforentrepreneurs.com/blog/install-redis-mac-and-linux)
  - Setup Redis on Remote Virtual Machine [blog post](https://www.codingforentrepreneurs.com/blog/remote-redis-servers-for-development/)
  - How I use Redis for new projects [short + code](https://www.codingforentrepreneurs.com/shorts/how-i-use-redis-for-new-projects-with-docker-compose/)
- A Bright Data Account [$25 credit for new accounts](https://brdta.com/justin)

## Getting Started

```bash
git clone https://github.com/codingforentrepreneurs/Django-Celery-Redis
mv Django-Celery-Redis scrape-scheduler
cd scrape-scheduler
```

`macos/linux`
```
python3 -m venv venv
source venv/bin/activate
```

`windows`
```
c:\Python311\python.exe -m venv venv
.\venv\Scripts\activate
```

Install requirements
```bash
python -m pip install pip --upgrade
python -m pip install -r requirements.txt
```

Run a local redis instance via Docker Compose
```bash
docker compose -f compose.yaml up -d
```
This will give us `redis://localhost:6170`

Create `.env` in `src/.env` with:

```bash
CELERY_BROKER_REDIS_URL="redis://localhost:6170"
DEBUG=True
```

Navigate into your Django root:

```bash
cd src/
ls
```
You should see at least `cfehome/` and `manage.py`.

Run your project in 2 terminals:
- `python manage.py runserver`
- `celery -A cfehome worker --beat`

Let's go!
