# Tugas 3 PBP Gasal 2023
### Annisa Az Zahra - 2106701242 - PBP A

## Link App Heroku
Nama App : app-annisa-tugas-2

[🌼 HTML Page](https://app-annisa-tugas-2.herokuapp.com/mywatchlist/html)

[🌸 JSON Page](https://app-annisa-tugas-2.herokuapp.com/mywatchlist/json)

[🌺 XML Page](https://app-annisa-tugas-2.herokuapp.com/mywatchlist/xml)

## Jawaban Soal

### ○ Perbedaan antara JSON, XML, dan HTML
JSON (JavaScript Object Notation) merupakan format pertukaran data yang cara penulisannya menggunakan objek JavaScript.  Format ini dapat digunakan untuk menyimpan, membaca, serta menukar informasi dari web server sehingga dapat dibaca oleh para pengguna. 

XML (Extensible Markup Language) merupakan bahasa markup yang seperti HTML namun didesain untuk menyimpan dan mengantarkan data. Strukturnya berbentuk seperti pohon dan memiliki tag-tag.

HTML (HyperText Markup Language) merupakan suatu bahasa markup yang digunakan untuk menampilkan tampilan halaman baik pada web ataupun web-app. Elemennya ditandai menggunakan tag-tag yang akan ditafsirkan oleh browser sehingga data dapat ditampilkan sesuai dengan tag yang digunakan

| Parameter | JSON | XML | HTML |
| ------------- | ------------- | ------------- | ------------- |
| Ekstensi File | .json | .xml | .html |
| Fungsi Utama | Menyimpan dan Mengirimkan Data | Menyimpan dan Mengirimkan Data | Menampilkan Data |
| Dukungan UTF | Mendukung encoding UTF dan ASCII | Mendukung encoding UTF-8 dan UTF-16 | Mendukung encoding UTF-8 dan UTF-16 (HTML5) |
| Bahasa | Format Javascript | Markup (Bukan bahasa pemrograman) | Markup (Bukan bahasa pemrograman) |
| Struktur penulisan | Menggunakan bracket "{ }" | Menggunakan tag "< >" dan wajib memiliki tag penutup | Menggunakan tag "< >" dan tidak wajib memiliki tag penutup | 
| Case-sensitive | Ya | Ya | Tidak |
| Kecepatan Transfer Data | Sangat cepat; karena menggunakan ruang memori yang sangat sedikit dan penguraian lebih cepat oleh mesin JavaScript | Lambat dalam penguraian data dan memorinya cukup besar | - |
| Keamanan | Penguraian JSON aman hampir sepanjang waktu kecuali jika JSONP digunakan | Struktur XML rentan terhadap beberapa serangan karena perluasan entitas eksternal dan validasi DTD diaktifkan secara default | - |


### ○ Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Suatu platform akan menggunakan data dari banyak sumber. Semakin kompleks dan dinamis implementasi web atau app, maka akan membutuhkan data yang makin banyak dan kompleks juga. Maka diperlukan stack lain untuk menyimpan data tersebut karena tidak mungkin semua data dituliskan satu persatu di dalam berkas 
`.html`. Pemisahan data ini juga berguna untuk memudahkan developer mengontrol suatu data dan me-maintain data yang akan ditampilkan. Data delivery inilah yang akan menjadi perantara komunikasi untuk mengirimkan data antar platform. 


### ○ Implementasi Checklist
1. Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu 
2. Menambahkan path mywatchlist pada `settings.py` di file [`settings.py`](project_django/settings.py).
    ```python
    INSTALLED_APPS = [
    ...
    'mywatchlist',
    ]
    ```
3. Membuat sebuah model `MyWatchList` pada [`models.py`](mywatchlist/models.py).
```python
class BarangMyWatchlist(models.Model):
    watched = models.TextField()
    title = models.CharField(max_length=200)
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()
   ```
4. Membuat berkas [`initial_mywatchlist_data.json`](mywatchlist/fixtures/initial_mywatchlist_data.json) untuk menambahkan 10 data untuk objek MyWatchList yang sudah dibuat di atas. Contoh salah satu datanya:
```json
[
....
{
  "model":"mywatchlist.barangmywatchlist",
  "pk":10,
  "fields":{
    "watched": "belum",
    "title":"Frozen",
    "rating": 4,
    "release_date": "29 November 2013",
    "review": "Dianimasikan dengan indah, ditulis dengan cerdas, dan diisi dengan lagu-lagu bernyanyi, Frozen menambahkan entri lain yang layak untuk Disney"
        }
},
....
]
```
5. Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format dengan membuat fungsi di [`views.py`](mywatchlist/views.py). Maisng-masing fungsi akan melakukan render masing-masing format data menggunakan data yang diambil dari database.
```python
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
```
6.  Membuat routing sehingga data di atas dapat diakses melalui URL dengan menambahkan berkas `urls.py` di folder `mywatchlist` dan melakukan routing dengan syntax:
```python
app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/', show_html, name='show_html'),
   
]
```

Kemudian juga membuat rotuting dengan menambahkan path di berkas `urls.py` pada folder `project_django`
```python
urlpatterns = [
    ...
    path('mywatchlist/', include('mywatchlist.urls')),
]
```

7.  App akan ter-deploy otomatis setelah di push

## Screenshot Postman
### HTML Response
#### Heroku
<img width="1440" alt="Screen Shot 2022-09-22 at 09 33 55" src="https://user-images.githubusercontent.com/73637698/191645642-495b9e51-d0ce-4f74-ab7c-c45f326cd540.png">

#### Local
<img width="1440" alt="Screen Shot 2022-09-22 at 09 43 45" src="https://user-images.githubusercontent.com/73637698/191646727-069fee50-5019-4eb9-a4a2-acfa7c8eba0c.png">

### JSON Response
#### Heroku
<img width="1440" alt="Screen Shot 2022-09-22 at 09 34 14" src="https://user-images.githubusercontent.com/73637698/191645652-ec6acb24-9eed-4461-a8e3-904c3c807da6.png">

#### Local
<img width="1440" alt="Screen Shot 2022-09-22 at 09 44 00" src="https://user-images.githubusercontent.com/73637698/191646923-bb4876ed-8fa9-4304-b236-e45de01cc0e6.png">


### XML Response
#### Heroku
<img width="1440" alt="Screen Shot 2022-09-22 at 09 34 03" src="https://user-images.githubusercontent.com/73637698/191645667-4e0f8a27-63f5-4140-96c9-32116f87d813.png">

#### Local
<img width="1440" alt="Screen Shot 2022-09-22 at 09 43 52" src="https://user-images.githubusercontent.com/73637698/191646760-47136f73-9564-4871-975d-8c9aba043375.png">




