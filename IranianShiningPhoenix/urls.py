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
from rest_framework.routers import DefaultRouter
from about.views import *
from contact.views import *
from products.views import *
from services.views import *
from category.views import *
from home.views import *

router = DefaultRouter()
router.register(prefix=r'about-us', viewset=AboutViewSet)
router.register(prefix=r'contact-us', viewset=ContactViewSet)
router.register(r'products-view', ProductViewSet)
router.register(r'services-view', ServicesViewSet)
router.register(r'category-view', CategoryViewSet)
router.register(r'slider', SliderViewSet)
router.register(r'CEO', CeoViewSet)


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("api-auth/", include("rest_framework.urls")),
                  path("api-token-auth/", obtain_auth_token),
                  path("api/", include(router.urls)),
                  path('home/', include("home.urls")),
                  path('contact/', include("contact.urls")),
                  path('about/', include("about.urls")),
                  path('products/', include('products.urls')),
                  path('services/', include('services.urls')),
                  path('category/', include('category.urls')),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
