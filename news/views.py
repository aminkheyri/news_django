from rest_framework.viewsets import ModelViewSet
from .models import NewsCeleryTasks
from .serializer import NewsSerializers


class NewsViewSet(ModelViewSet):
    queryset = NewsCeleryTasks.objects.all()
    serializer_class = NewsSerializers
