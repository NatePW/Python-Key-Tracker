from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from Keys.models import Key

def index(request):
    all_keys = Key.objects.order_by('name')
    template = loader.get_template('Keys/index.html')
    context = RequestContext(request, {
        'all_keys': all_keys,
        'out': 1,
    })
    return HttpResponse(template.render(context))