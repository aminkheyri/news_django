from django.db import models
from .tasks import get_varzesh3_information



class NewsCeleryTasks(models.Model):
    task_id = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='news_pics/%Y/%m/%d', null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    lastmod = models.DateTimeField(null=True, blank=True)
    content = models.TextField(null=True, blank=True) 



