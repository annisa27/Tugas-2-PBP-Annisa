from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_katalog,
        'nama': 'Annisa Az Zahra',
        'npm': '2106701242'
    }
    return render(request, "katalog.html", context)