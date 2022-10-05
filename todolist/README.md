# Tugas 4 PBP Gasal 2023
### Annisa Az Zahra - 2106701242 - PBP A

## Link App Heroku
Nama App : app-annisa-tugas-2

[🌸 App Page](https://app-annisa-tugas-2.herokuapp.com/todolist/)

## Jawaban Soal

### ○ Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
Fungsi dari `{% csrf_token %}` adalah sebagai pertahanan yang disediakan Django untuk menahan seranagn CSRF (Cross Site Request Forgeries). CSRF adalah serangan yang membuat pengguna website tanpa sadar mengirimkan request kepada aplikasi website sehingga aplikasi tersebut mengeksekusi request yang sebenarnya tidak dikirimkan oleh user. Maka, `{% csrf_token %}` ini akan mencegah hal tersebut terjadi dengan membuat token di server saat merender halaman dan akan memeriksa token setiap ada rquest yang masuk. Request hanya akan diekseskusi jika terdapat token yang dibuat ini. Jika suatu request tidak terdapat tokennya, maka request tersebut akan ditolak dan tidak diekseskusi. 

Apabila kita tidak menyertakan potongan kode `{% csrf_token %}` pada elemen `<form>`, akan muncul Error 403 Forbidden dengan keterangan "CSRF verification failed. Request aborted." karena CSRF Tokennya tidak dapat ditemukan.Sehingga, user tidak dapat mengakses halaman HTMLnya

### ○ Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Tentu saja kita dapat membuat elemen `<form>` secara manual dengan memanfaatkan elemen `<input>` pada `.html`. Pertama, kita dapat mendefinisikan elemen `<form>` terlebih dahulu, kemudian di dalam tag `<form>` kita dapat mendefinisikan elemen `<label>` sebagai pendanda input dan `<input>` sebagai tempat user mengisikan data dengan text area, radio button, atau tipe lain. Input ini dapat disesuaikan keperluannya, setidaknya terdapat 22 tipe input. Tipe input yang digunakan pada tugas ini adalah text, password, dan submit untuk melakukan action yang telah didefinisikan pada elemen `<form>`.

Kemudian jika ingin tampilan form dapat lebih rapih, kita dapat emnggunakan elemen `<table>`. Kemudian, untuk mengisi data dari table tersebut kita dapat menggunakan elemen `<tr>` untuk mendefinisikan data di suatu row atau baris, kemudian di elemen tersebut kita definisikan lagi `<td>` atau table data yang ingin kita letakkan. Pada `<td>` inilah kita juga menggunakan elemen `<input>` sebagai text field area user memasukan suatu input untuk form. Berikut adalah potongan kode contoh form sederhana:

```html
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname">
</form>
```

### ○ Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Ketika pengguna melakukan submisi terhadap HTML form yang telah diisi, browser akan membuat HTTP Request, method, dan argumen yang diterima ke destinasi URL berdasarkan halaman `.html` dari form. HTTP Request ini akan dikirimkan oleh browser ke server dengan method POST, hal ini akan melakukan perubahan terhadap database server. Ketika server telah menerima dan menyimpan HTTP Request yang dikirimkan, server akan mengecek apakah request yang request yang dikirimkan valid. Setelah itu, server akan melihat method mana pada views.py yang cocok untuk meng-handle request yang dikirimkan. Ketika menemukan method yang cocok, Django views akan merespon dengan mengembalikan HTTP Response dan memproses data yang dikirimkan menjadi halaman `.html`. 


### ○ Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya dengan command `python manage.py startapp todolist`

2.  Menambahkan path todolist pada `settings.py` di file [`settings.py`](project_django/settings.py).
    ```python
    INSTALLED_APPS = [
    ...
    'todolist',
    ]
    ```

3. Membuat sebuah model `Task` pada [`models.py`](todolist/models.py).
```python
class ToDoList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()
   ```

Kemudian, dijalankan perintah `python manage.py makemingrations` dan `python manage.py migrate` untuk melakukan migrasi skema model

4. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan pada [`views.py`](todolist/models.py).
  ```python
  @login_required(login_url='login/')
  def show_todolist(request):
    ...

  def register(request):
    ...

  def login_user(request):
    ...

  def logout_user(request):
    ...

  def create_task(request):
    ...
  ```

5. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
Saya membuat berkas [`todolist.html`](todolist/templates/todolist.html). Pada halaman ini, tiap task yang dibuat akan diambil dan ditampilkan pada tabel.


6. Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.
Saya membuat berkas [`create.html`](todolist/templates/create.html). 

7. Membuat routing sehingga beberapa fungsi dapat diakses.
```python
  app_name = 'todolist'

  urlpatterns = [
      path('', show_todolist, name="show_todolist"),
      path('register/', register, name='register'),
      path('login/', login_user, name='login'), 
      path('logout/', logout_user, name='logout'),
      path('create-task/', create_task, name='create_task')
  ]
```

8. Deployment dilakukan secara otomatis ketika saya melakukan push ke repositori karena saya telah mendaftarkan HEROKU_API_KEY dan HEROKU_APP_NAME sebagai secrets

9. Dummy akun yang dibuat dengan masing-masing 3 task
  ```
  username_1: annisa
  password_1: icune123
  
  username_2: diana
  password_2: kiyowo123
  ```

