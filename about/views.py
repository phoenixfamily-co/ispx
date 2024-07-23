from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView


# Create your views here.
@cache_page(60 * 15)
def about_view(request):
    template = loader.get_template('about.html')

    return HttpResponse(template.render(request))

