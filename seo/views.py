# from django.shortcuts import render
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from IranianShiningPhoenix.permissions import IsSuperUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsSuperUser]

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        count, _ = Article.objects.all().delete()
        return Response(f"All {count} Article instances were deleted.", status=status.HTTP_204_NO_CONTENT)
