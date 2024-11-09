from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from IranianShiningPhoenix import settings
from .views import ServicesViewSet , services_view

router = DefaultRouter()
router.register(r'services-view', ServicesViewSet)
# use http://127.0.0.1:8000/services/services-view/delete_all/ with method DELETE to call delete_all function
# for filter services by category: http://127.0.0.1:8000/services/services-view/by_category/?category_id=3
# in services app for filtering by category i create a custom action using action decorator in views.py

app_name = 'services'

urlpatterns = [
    path('api/', include(router.urls)),
    path("<int:pk>/", services_view, name='services_view'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
