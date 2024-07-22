from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(prefix=r'about-us', viewset=AboutViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # use http://127.0.0.1:8000/about/about-us/delete_all/ with method DELETE to call delete_all function
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
