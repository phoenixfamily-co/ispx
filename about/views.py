from django.shortcuts import render
from rest_framework import viewsets
from .models import About
from .serializers import AboutSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    # create a delete all method using action decorator, use http://127.0.0.1:8000/about/about-us/delete_all/ with
    # method DELETE to call delete_all function
    @action(detail=False, methods=['delete', ])
    def delete_all(self, request):
        count, _ = About.objects.all().delete()
        return Response(f"All {count} About instances were deleted.", status=status.HTTP_204_NO_CONTENT)
