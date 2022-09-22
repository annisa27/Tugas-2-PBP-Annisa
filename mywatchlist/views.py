from mywatchlist.models import BarangMyWatchlist
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers


# TODO: Create your views here.
def show_mywatchlist(request):
    item_mywatchlist = BarangMyWatchlist.objects.all()
    context = {
        'item_mywatchlist': item_mywatchlist,
        'nama' : 'Annisa',
        'npm' : '2106701242',
    }
    return render(request, 'mywatchlist.html', context)

def show_xml(request):
    data = BarangMyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = BarangMyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    data = BarangMyWatchlist.objects.all()
    context = {
        'item_mywatchlist': data,
        'nama' : 'Annisa',
    }
    return render(request, 'mywatchlist.html', context)