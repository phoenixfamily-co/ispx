from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from rest_framework import generics
from .models import Slider, CEO
from .serializers import SliderSerializer, CeoSerializer
from django.template import loader


@cache_page(60 * 15)
def home_view(request):
    template = loader.get_template('home.html')
    context = {}

    return HttpResponse(template.render(context, request))


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
