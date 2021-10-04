from rest_framework import viewsets
from .models import News
from .serializer import NewsSerializers


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
