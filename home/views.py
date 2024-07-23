from django.http import HttpResponse
from django.template import loader
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def home_view(request):
    template = loader.get_template('home.html')
    context = {}

    return HttpResponse(template.render(context, request))
