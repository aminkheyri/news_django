from django.db import models
from django.db.models.fields import TextField


class News(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='news_pics/%Y/%m/%d')
    lastmod = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
