from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import home_view, SliderListCreateAPIView, SliderRetrieveUpdateDestroyAPIView, CeoListCreateAPIView, \
    CeoRetrieveUpdateDestroyAPIView


app_name = 'home'


urlpatterns = [
    path("", home_view, name='view'),
    path("sliders/", SliderListCreateAPIView.as_view(), name='customer-list-create'),
    path("ceo/", CeoListCreateAPIView.as_view(), name='ceo-list-create'),
    path("sliders/<int:pk>/", SliderRetrieveUpdateDestroyAPIView.as_view(), name='customer-detail'),
    path("ceo/<int:pk>/", CeoRetrieveUpdateDestroyAPIView.as_view(), name='ceo-detail'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
