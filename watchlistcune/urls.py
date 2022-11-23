from django.urls import path
from watchlistcune.views import show_mywatchlist
from watchlistcune.views import show_xml
from watchlistcune.views import show_json
from watchlistcune.views import show_html

app_name = 'watchlistcune'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/', show_html, name='show_html'),
   
]