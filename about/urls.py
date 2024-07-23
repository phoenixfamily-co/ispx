from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import AboutView

urlpatterns = [
    path("", AboutView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)