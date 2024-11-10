from django.http import HttpResponse
from django.template import loader
from django.views.decorators.cache import cache_page
from rest_framework import viewsets

from category.models import Category
from .models import Services
from .serializers import ServicesSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from IranianShiningPhoenix.permissions import IsSuperUser


# Create your views here.

@cache_page(60 * 15)
def services_view(request, pk):
    template = loader.get_template('services.html')
    category = Category.objects.all()
    services = Services.objects.filter(categories=pk)
    context = {
        'category': category,
        'services': services
    }
    return HttpResponse(template.render(context, request))


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsSuperUser]

    # use http://127.0.0.1:8000/services/services-view/delete_all/ with method DELETE to call delete_all function
    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        count, _ = Services.objects.all().delete()
        return Response(f"All {count} Services instances were deleted.", status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category_id = request.query_params.get('category_id')
        if category_id is not None:
            services = self.queryset.filter(categories__id=category_id)
            serializer = self.get_serializer(services, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "category_id query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
