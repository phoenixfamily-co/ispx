from django.shortcuts import render
from rest_framework import viewsets
from .models import Services
from .serializers import ServicesSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        count, _ = Services.objects.all().delete()
        return Response(f"All {count} Services instances were deleted.", status=status.HTTP_204_NO_CONTENT)
