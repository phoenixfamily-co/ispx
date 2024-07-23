from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import about_view, AboutViewSet

app_name = 'about'

router = DefaultRouter()
router.register(prefix=r'about-us', viewset=AboutViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("", about_view, name='view'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
