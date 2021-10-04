from .models import News
from rest_framework import serializers


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = {'id', 'title', 'image','body', 'lastmod'}