from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServicesViewSet

router = DefaultRouter()
router.register(r'services-view', ServicesViewSet)
# use http://127.0.0.1:8000/services/services-view/delete_all/ with method DELETE to call delete_all function
# for filter services by category: http://127.0.0.1:8000/services/services-view/by_category/?category_id=3
# in services app for filtering by category i create a custom action using action decorator in views.py

urlpatterns = [
    path('', include(router.urls)),
]
