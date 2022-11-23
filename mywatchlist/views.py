from mywatchlist.models import BarangMyWatchlist
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse


from mywatchlist.models import BarangMyWatchlist


# TODO: Create your views here.
def show_mywatchlist(request):
    item_mywatchlist = BarangMyWatchlist.objects.all()
    context = {
        'item_mywatchlist': item_mywatchlist,
        'nama' : 'Annisa',
        'npm' : '2106701242',
        'message' : message()
    }
    return render(request, 'mywatchlist.html', context)

def show_xml(request):
    data = BarangMyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = BarangMyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def goals_by_data(request, format):
    data = BarangMyWatchlist.objects.all()
    if format == 'json':
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    elif format == 'xml':
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    else:
        return HttpResponse('No Goals Found')

def show_html(request):
    data = BarangMyWatchlist.objects.all()
    context = {
        'item_mywatchlist': data,
        'nama' : 'Annisa',
        'npm' : '2106701242',
        'message' : message()
    }
    return render(request, 'mywatchlist.html', context)

def message():
    watched = BarangMyWatchlist.objects.all().values("watched")
    sudah, all_list = 0,0

    for i in watched:
        all_list += 1
        if i['watched'] == True:
            sudah += 1

    if sudah >= all_list-sudah:
        return "Selamat, kamu sudah banyak menonton!"
    return "Wah, kamu masih sedikit menonton!"