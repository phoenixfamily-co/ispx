from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products-view', ProductViewSet)
# products bulk delete: http://127.0.0.1:8000/products/products-view/delete_all/
# for filter products by category: http://127.0.0.1:8000/products/products-view/?categories=2
# in product app for filtering by categories developed by django-filter package in view.py

urlpatterns = [
    path('', include(router.urls)),
]
