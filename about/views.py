from django.http import HttpResponse
from django.template import loader
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60 * 15)
def about_view(request):
    template = loader.get_template('about.html')
    context = {}

    return HttpResponse(template.render(context, request))
