from rest_framework.viewsets import ModelViewSet
from .models import News
from .serializer import NewsSerializers


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
