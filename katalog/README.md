# Tugas 2 PBP Gasal 2023
### Annisa Az Zahra - 2106701242 - PBP A

## Link App Heroku
Nama App : app-annisa-tugas-2

[🏠 Landing Page](https://app-annisa-tugas-2.herokuapp.com/)

[🛒 Catalog Page](https://app-annisa-tugas-2.herokuapp.com/katalog/)

## Jawaban Soal

  ### ○ Bagan Django Request Client & Response Cycle
<img width="1344" alt="Bagan_AnnisaAzZahra_2106701242" src="https://user-images.githubusercontent.com/73637698/190141078-a36f742e-d0a6-4d7e-bc3a-94ffa2f75f21.png">
  
  **Kaitan antara `urls.py`, `views.py`, `models.py`, dan `berkas .html`**
  Pada gambar di atas, ketiga berkas .py dan berkas .html berhubungan satu sama lain.
  1. Client akan mengirimkan request ke dalam server DJango dengan mengakses URL. Kemudian request yang masuk akan diproses oleh `urls.py` yang berfungsi sebagai router.
  2. Request yang telah masuk pada `urls.py` akan diteruskan dan dicocokkan ke `views.py`. Kemudian akan dipanggil fungsi pada `views.py` yang sesuai.
  3. `views.py` akan memanggil query ke `models.py` ketika ada aktivitas (read atau write) yang melibatkan database
  4. Akan terjadi transaksi data yang dibutuhkan dari database
  5. `views.py` akan mencari file `<filename>.html` yang sesuai dengan request client
  6. `views.py`akan meneruskan respon HTML kepada client
  

  ### ○ Penggunaan Virtual Environment pada Django
  **1. Jelaskan kenapa menggunakan virtual environment?**
  
  Suatu virtual environment memungkinkan developer untuk membuat project yang berbeda-beda dengan dependencies yang berbeda-beda dalam suatu device atau
  sistem operasi. Virtual environment ini akan membuat environment masing-masing untuk tiap project atau app, sehingga akan menghindari konflik dengan
  sistem operasi utama yang sedang digunakan. Selain itu, virtual envinronment akan menginstall packages dan dependencies secara otomatis.
  
  Sebagai contoh, misalnya pada device yang kita gunakan, kita menginstall Django versi 3.2. Namun, kita sedang mengerjakan project dengan Django versi 1.7
  Hal ini dapat diatasi dengan adanya virtual environment. Kita dapat mengerjakan project dengan Django 1.7 di device dengan Django 3.2 tanpa mengalami
  konflik dengan menggunakan virtual environment.
  
  Virtual Environment juga memudahkan mobilisasi atau perpindahan project antar device. Jadi, seorang developer dapat dengan mudah mengerjakan projectnya
  tanpa melakukan konfigurasi ulang.
   
  
  **2. Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
  
  Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment namun tentunya akan rawan terjadi konflik dan agak sulit
  untuk melakukan mobilisasi seperti yang saya jelaskan pada pertanyaan sebelumnya
  
  ### ○ Implementasi Poin 1 - 4
  1. Membuat sebuah fungsi pada `views.py` yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
  
  Fungsi yang saya buat pada [`views.py`](katalog/views.py). adalah fungsi `show_catalog(request)` yang berfungsi untuk melakukan query dari data `.json`.
  Semua data dari `.json` diambil dari syntax `data_barang_katalog = CatalogItem.objects.all()` kemudian data yang telah diambil dikembalikan (return) ke     template .html menggunakan function `render()`
  ```python
   def show_catalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_katalog,
        'nama': 'Annisa Az Zahra',
        'npm': '2106701242'
    }
    return render(request, "katalog.html", context)
   ```
   2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada [`views.py`](katalog/views.py).
   
   Bagian ini dilakukan dengan menambahkan path routing pada file `urls.py` [katalog](katalog) dan [project_django](project_django)

   Pada [katalog](katalog)
   ```python
      urlpatterns = [
          path('', show_catalog, name='show_catalog'),
      ]
   ```
   
   Pada [project_django](project_django)
   ```python
      urlpatterns = [
          . . .
          path('katalog/', include('katalog.urls')),
      ]
   ```

   3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
   
   Setelah data sudah dimuat dengan command  `python manage.py loaddata initial_wishlist_data.json`, dibuat variabel `context` yang akan menyimpan data
   yang di-load. Kemudian variabel `context` akan menjadi parameter dari function `render()`. 
   
   Kemudian data ini akan ditampilkan pada [katalog.html](katalog/templates) dengan iterasi items yang terdapat pada [models.py](katalog/models.py)
   ```python
      {% for barang in list_barang %}
        <tr>
            <th>{{barang.item_name}}</th>
            <th>{{barang.item_price}}</th>
            <th>{{barang.item_stock}}</th>
            <th>{{barang.description}}</th>
            <th>{{barang.rating}}</th>
            <th>{{barang.item_url}}</th>
        </tr>
      {% endfor %}
   ```
   
   4. Melakukan deployment ke Heroku
  
   Setelah membuat app khusus untuk deploy, tambahkan `repository secret` pada repositori yakni dengan menambahkan App Name dan API Key. 
   Selanjutnya cukup lakukan `add`, `commit`, `push` perubahan yang telah dibuat, pada menu Actions pun dapat dilihat aktivitas deploy dari app.

  ### Source
  > Rekaman kelas PBP A - Selasa, 14 September 2022 (https://drive.google.com/drive/folders/12NE5Dr2ujyVZYjI7RmaJIB9VaMh_mRFj)
  > https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-1/

