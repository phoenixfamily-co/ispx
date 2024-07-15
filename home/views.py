from django.views.generic import TemplateView
from rest_framework import generics
from .models import Slider, CEO
from .serializers import SliderSerializer, CeoSerializer


class WelcomeView(TemplateView):
    template_name = "main.html"


class SliderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class SliderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class CeoListCreateAPIView(generics.ListCreateAPIView):
    queryset = CEO.objects.all()
    serializer_class = CeoSerializer


class CeoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CEO.objects.all()
    serializer_class = CeoSerializer
