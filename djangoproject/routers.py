from django.db import router
from rest_framework import routers
from news.views import NewsSerializers


router = routers.SimpleRouter()
router.register('news', NewsSerializers, basename='news')

