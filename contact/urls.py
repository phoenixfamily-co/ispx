from django.urls import path, include
from .views import ContactViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix=r'', viewset=ContactViewSet)

urlpatterns = [
    path('contact-us/', include(router.urls)),
]
