from django.conf.urls.static import static
from django.urls import path, include

from IranianShiningPhoenix import settings
from .views import ContactViewSet, contact_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix=r'contact-us', viewset=ContactViewSet)

app_name = 'contact'

urlpatterns = [

    path("", contact_view, name='view'),
    path('api/', include(router.urls)),

]

urlpatterns += router.urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
