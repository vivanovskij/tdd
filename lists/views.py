from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item


def home_page(request):
    '''домашняя страница'''
    if request.method == 'POST':
        Item.objects.create(text=request.POST.get(
            'item_text', 'views.home_page'))
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
