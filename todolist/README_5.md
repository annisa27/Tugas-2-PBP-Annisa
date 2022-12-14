# Tugas 5 PBP Gasal 2023
### Annisa Az Zahra - 2106701242 - PBP A

## Link App Heroku
Nama App : app-annisa-tugas-2

[🌸 App Page](https://app-annisa-tugas-2.herokuapp.com/todolist/)

## Jawaban Soal

### ○ Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Perbedaan antara Inline, Internal, dan External CSS hanya terdapat dari cara peletakannya saja. Inline CSS adalah kode CSS yang dituliskan langsung pada atribut elemen HTML, tepatnya di dalam atribut `style=""`. Sedangkan Internal CSS adalah kode CSS yang ditulis di dalam tag `<style>` di dalam file HTML. Sedangkan External CSS adalah kode CSS yang ditulis terpisah dengan kode HTML dan dituliskan ke dalam file `.css`, file `.css` ini biasanya didefinisikan di bagian `<head>` di dalam file `.html` yang ingin diberikan style css.

| Implementasi CSS | Kelebihan | Kekurangan | 
| ------------- | ------------- | ------------- |
| Inline style | Lebih cepat karena tidak perlu membuat id dan class atau melakukan selector | Sangat tidak efisien karena seorang developer harus menuliskan style satu per satu elemen yang berbeda dengan style yang sama (redundant) | 
|  | Proses HTTP Request lebih kecil, sehingga load website akan lebih cepat |  |
|  | Berguna untuk menguji tampilan satu elemen saja |  |
| Internal style sheet | Perubahan hanya berlaku di satu halaman dan satu elemen saja, sehingga dapat membuat tiap halaman web menjadi unik berbeda satu sama lain | Performa website akan lebih lambat, jika menggunakan internal css yang berbeda-beda untuk seluruh halaman hal ini akan menyebabkan loading ulang setiap pengguna bernavigasi antar halaman website | 
|  | Lebih efisien daripada inline style karena bisa menggunakan selector css | Namun, tetap kurang efisien jika ingin menggunakan style css yang sama dalam |
|  | Developer tidak perlu meng-upload banyak file, karena html dan cssnya sudah terintegrasi dalam satu file .html |  |
| External style sheet | Ukuran file HTML akan lebih kecil dan strukturnya akan lebih rapih. Sehingga memudahkan orang lain untuk mengerti struktur dari website yang sedang dikembangkan | Jika file css gagal dipanggil oleh file HTML dikarenakan koneksi internet pengguna yang lambat, hal in iakan menyebabkan halama HTML menjadi berantakan | 
|  | Loading website akan lebih cepat |  |
|  | Satu file css dapat digunakan oleh banyak halaman website |  |

Kesimpulannya, untuk memudahkan maintenence pada suatu project html dan css, lebih disarankan untuk menggunakan External CSS saja.

### ○ Jelaskan tag HTML5 yang kamu ketahui.

Pada HTML5, ada banyak sekali tag yang dapat digunakan untuk mendefinisikan struktur suatu halaman

| Group Tag | Tag | Fungsi | 
| ------------- | ------------- | ------------- |
| Tag Dasar | `<! DOCTYPE html>` | Deklarasi untuk mendefinisikan dokumen menjadi HTML |
| | `<html>` | Tag pembuka untuk membuat dokumen HTML |
| | `<head>` | Tag untuk mendifinisikan informasi meta, import css, import font, dan lain-lain. |
| | `<title>` | Tag untuk menampilkan judul di tab browser |
| | `<body>` | Tag untuk meletakkan semua konten website |
| Tag Teks | `<h1> - <h6>` | Membuat heading pada suatu halaman |
|  | `<p>` | Membuat paragraf atau teks ukuran default pada suatu halaman |
|  | `<br>` | Membuat garis baru |
|  | `<pre>` | Memformat teks atau kalimat |
|  | `<hr>` | Memisahkan antar konten dan elemen |
| Tag Formatting | `<b>` | Membuat teks bold |
|  | `<p>` | Membuat paragraf atau teks ukuran default pada suatu halaman |
|  | `<i>` | Membuat teks miring |
|  | `<small>` | Membuat teks kecil |

Dan masih banyak tag lain yang dapat digunakan



### ○ Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Secara garis besar, suatu elemen HTML bisa diakses dengan tiga tipe CSS Selector, yakni element selector, class selector, dan id selector.
| Tipe Selector | Penjelasan | Contoh | 
| ------------- | ------------- | ------------- |
| Element Selector | Ditulis tanpa menggunakan leading baik `#` atau `.` selector ini disesuaikan dengan tag-tag pada file HTML yang ingin diberikan style | `p { ... }` selector ini akan memilih semua elemen dengan tag `<p>` |
| Class Selector | Ditulis dengan menggunakan leading `.` developer harus mendefinisikan atribut `class=""` kemudian nama dari class yang telah dibuat dapat digunakan pada penulisan CSS | Contohnya developer mendefinisikan atribut class sebagai `class="hero"`. Maka pada file css, developer dapat memanggil `.hero{ ... }` selector ini akan memilih semua elemen dengan class hero |
| ID Selector | Ditulis dengan menggunakan leading `#` developer harus mendefinisikan atribut `id=""` kemudian nama dari id yang telah dibuat dapat digunakan pada penulisan CSS | Contohnya developer mendefinisikan atribut id sebagai `id="maincontent"`. Maka pada file css, developer dapat memanggil `#maincontent{ ... }` selector ini akan memilih semua elemen dengan id maincontent |

### ○Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pertama saya mengimport bootstrap ke setiap file .html saya untuk memanfaatkan framewrok bootstrap dengan meletakkan 
` <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">` pada bagian block meta, sebenarnya hal ini cukup dilakukan pada bagian `extends.html` saja, namun cara ini tidak berhasil pada saya.  

Kemudian saya mengimplementasi inline css untuk hampir ke setiap tag html yang terdapat pada filenya. Saya memanfaatkan atribut dan class di bootstrap untuk melakukan styling terhadap elemen HTML yang didefinisikan.

Untuk halaman `login.html`, `create.html`, dan `register.html` kurang lebih memiliki struktur yang sama, peletakannya menggunakan class container dan row. 

Untuk halaman `todolist.html` saya membuat tiap task syntax for, kemudian tiap task tersebut akan di generate dalam bentuk card. Implementasi card ini saya memanfaatkan class pada boostrap juga sehingga akan otomatis terbentuk. Tiap card ini disusun dalam display grid. 
```html
    <div >
    <div >
        <div  class="card-grid" style=" display: grid; grid-template-columns: auto auto auto auto; gap: 10px; padding: 10px;">
        {% if todo %}
        {% for task in todo %}
        <div class="card" style="margin:2%;">
            <div class="card-header" style="background-color: rgb(195, 107, 184);">
            ...
            </div>

            <div class="card-body">
            ...
            </div>
            
            <div class="card-footer">
            ...
            </div>
        </div>

        {% endfor %}
        {% else %}
        {% endif %}
    </div>
    </div>
    </div>
```

Untuk membuat keempat halaman yang dikustomisasi menjadi responsive, saya cukup memanfaatkan framework dari bootstrap yang telah menyediakan fitur responsiveness. Kemudian, untuk ukuran masing-masing element saya menggunakan satuan `%` dan `rem` agar lebih responsive.

Sumber:
> https://www.niagahoster.co.id/blog/perbedaan-internal-external-dan-inline-css/

> PPT PBP - Slide 6: Web Design Using HTML5 and CSS3