from django.shortcuts import render

from amazonsearchapp.models import Item

def amazon_search(request):
    item_obj = Item.objects.filter()

    context = {
        "items": item_obj
    }

    return render(request, 'results.html', context)