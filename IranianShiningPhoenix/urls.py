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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from about.views import *
from contact.views import *
from products.views import *
from services.views import *
from category.views import *
from home.views import *
from IranianShiningPhoenix import settings


urlpatterns = [

    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api-token-auth/", obtain_auth_token),
    path('home/', include("home.urls", namespace='home')),
    path('contact/', include("contact.urls", namespace='contact')),
    path('about/', include("about.urls", namespace='about')),
    path('products/', include('products.urls', namespace='products')),
    path('services/', include('services.urls', namespace='services')),
    path('category/', include('category.urls', namespace='category')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
