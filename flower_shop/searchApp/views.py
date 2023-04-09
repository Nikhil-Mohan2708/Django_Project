from django.shortcuts import render
from flowerApp.models import Flower
from django.db.models import Q
# Create your views here.


def SearchResult(request):
    query = None
    flowers = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        flowers = Flower.objects.all().filter(Q(name__contains=query))
        return render(request, 'search.html', {'query':query, 'flowers':flowers})