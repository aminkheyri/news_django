from rest_framework.routers import SimpleRouter
from news.views import NewsViewSet


router = SimpleRouter()
router.register('news', NewsViewSet, basename='news')

