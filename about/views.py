from django.http import HttpResponse
from django.template import loader
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from about.models import About
from about.serializers import AboutSerializer
from IranianShiningPhoenix.permissions import IsSuperUser


# Create your views here.
@cache_page(60 * 15)
def about_view(request):
    template = loader.get_template('about.html')
    context = {}

    return HttpResponse(template.render(context, request))


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsSuperUser]

    # create a delete all method using action decorator, use http://127.0.0.1:8000/about/about-us/delete_all/ with
    # method DELETE to call delete_all function
    @action(detail=False, methods=['delete', ])
    def delete_all(self, request):
        count, _ = About.objects.all().delete()
        return Response(f"All {count} About instances were deleted.", status=status.HTTP_204_NO_CONTENT)