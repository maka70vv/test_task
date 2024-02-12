from django.shortcuts import render
from django.core.cache import cache
from .models import MenuItem


def output(request):
    menu_items = cache.get('menu_items')
    if not menu_items:
        menu_items = MenuItem.objects.all()
        cache.set('menu_items', menu_items)
    return render(request, 'output.html', {'menus': menu_items, 'request': request})
