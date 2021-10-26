from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .routers import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('test/', include('news.urls', namespace='test'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)