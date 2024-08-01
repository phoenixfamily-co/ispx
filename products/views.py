from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from IranianShiningPhoenix.permissions import IsSuperUser

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categories']
    permission_classes = [IsSuperUser]

    @action(detail=False, methods=['DELETE'])
    def delete_all(self, request):
        count, _ = Product.objects.all().delete()
        return Response(f"All {count} product instances were deleted.", status=status.HTTP_204_NO_CONTENT)
