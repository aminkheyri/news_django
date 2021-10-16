from django.urls import path
from .views import Test1Serializer


app_name = 'test'
urlpatterns = [
    path('test1', Test1Serializer.as_view(), name='test1')
]