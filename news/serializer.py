from .models import NewsCeleryTasks
from rest_framework import serializers


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsCeleryTasks
        fields = ('title', 'image','body', 'lastmod')