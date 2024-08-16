from django.urls import path, include
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix=r'article-view', viewset=ArticleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]