from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from .models import NewsCeleryTasks
from .serializer import NewsSerializers
from .tasks import get_varzesh3_information


class NewsViewSet(ModelViewSet):
    queryset = NewsCeleryTasks.objects.all()
    serializer_class = NewsSerializers



class Test1Serializer(ListCreateAPIView):
    queryset = NewsCeleryTasks.objects.all()
    serializer_class = NewsSerializers

    