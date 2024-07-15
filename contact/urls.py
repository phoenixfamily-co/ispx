from django.urls import path
from .views import ContactCreateAPIView

urlpatterns = [
    path('inform-us/', ContactCreateAPIView.as_view(), name='contact-create'),
]
