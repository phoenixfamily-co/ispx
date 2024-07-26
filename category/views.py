from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        count, _ = Category.objects.all().delete()
        return Response(f"All {count}, category instances were deleted.", status=status.HTTP_204_NO_CONTENT)
