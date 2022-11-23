from django.shortcuts import render
from mywatchlist.models import BarangMyWatchlist
from django.http import HttpResponse
from django.core import serializers


# TODO: Create your views here.
def show_mywatchlist(request):
    item_mywatchlist = BarangMyWatchlist.objects.all()
    belum_tonton = 0
    watched = 0 
    pesan = ""
    for film in item_mywatchlist:
        if (film.watched ):
            watched += 1
        else:
            belum_tonton += 1
    if (watched >= belum_tonton):
        pesan = "Selamat, kamu sudah banyak menonton!"
    else:
        pesan = "Wah, kamu masih sedikit menonton!"
    context = {
        'item_mywatchlist': item_mywatchlist,
        'nama' : 'Annisa',
        "pesan" : pesan,
    }
    return render(request, 'mywatchlist.html', context)


def show_xml(request):
    data = BarangMyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = BarangMyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    item_mywatchlist = BarangMyWatchlist.objects.all()
    belum_tonton = 0
    watched = 0 
    pesan = ""
    for film in item_mywatchlist:
        if (film.watched):
            watched += 1
        else:
            belum_tonton += 1
    if (watched >= belum_tonton):
        pesan = "Selamat, kamu sudah banyak menonton!"
    else:
        pesan = "Wah, kamu masih sedikit menonton!"
    context = {
        'item_mywatchlist': item_mywatchlist,
        'nama' : 'Annisa',
        "pesan" : pesan,
    }
    return render(request, 'mywatchlist.html', context)
