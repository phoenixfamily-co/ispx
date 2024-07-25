from django.urls import path, include
from .views import ContactViewSet,contract_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix=r'', viewset=ContactViewSet)

app_name = 'contract'


urlpatterns = [
    path('contact-us/', include(router.urls)),
    path("", contract_view, name='view'),

]
