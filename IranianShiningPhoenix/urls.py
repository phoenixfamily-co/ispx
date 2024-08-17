"""
URL configuration for IranianShiningPhoenix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .permissions import IsSuperUser
from django.contrib.auth import views as auth_views

# from rest_framework.routers import DefaultRouter
# from about.views import *
# from contact.views import *
# from products.views import *
# from services.views import *
# from category.views import *
# from home.views import *
# from seo.views import ArticleViewSet
#
# router = DefaultRouter()
# router.register(prefix=r'about-us', viewset=AboutViewSet)
# router.register(prefix=r'contact-us', viewset=ContactViewSet)
# router.register(r'products-view', ProductViewSet)
# router.register(r'services-view', ServicesViewSet)
# router.register(r'category-view', CategoryViewSet)
# router.register(r'slider', SliderViewSet)
# router.register(r'CEO', CeoViewSet)
# router.register(r'seo', ArticleViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="ISPX APIs",
        default_version='v1',
        description="API docs",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mohammadmma3004@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=[IsSuperUser],
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("api-auth/", include("rest_framework.urls")),
                  path("api-token-auth/", obtain_auth_token),
                  # path("api/", include(router.urls)),
                  path('home/', include("home.urls")),
                  path('contact/', include("contact.urls")),
                  path('about/', include("about.urls")),
                  path('products/', include('products.urls')),
                  path('services/', include('services.urls')),
                  path('category/', include('category.urls')),
                  path('seo/', include('seo.urls')),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
                       name='schema-swagger-ui'),
                  path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
