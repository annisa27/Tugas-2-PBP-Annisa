# Tugas 4 PBP Gasal 2023
### Annisa Az Zahra - 2106701242 - PBP A

## Link App Heroku
Nama App : app-annisa-tugas-2

[🌸 App Page](https://app-annisa-tugas-2.herokuapp.com/todolist/)

## Jawaban Soal

### ○ Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
Fungsi dari `{% csrf_token %}` adalah sebagai pertahanan yang disediakan Django untuk menahan seranagn CSRF (Cross Site Request Forgeries). CSRF adalah serangan yang membuat pengguna website tanpa sadar mengirimkan request kepada aplikasi website sehingga aplikasi tersebut mengeksekusi request yang sebenarnya tidak dikirimkan oleh user. Maka, `{% csrf_token %}` ini akan mencegah hal tersebut terjadi dengan membuat token di server saat merender halaman dan akan memeriksa token setiap ada rquest yang masuk. Request hanya akan diekseskusi jika terdapat token yang dibuat ini. Jika suatu request tidak terdapat tokennya, maka request tersebut akan ditolak dan tidak diekseskusi. 

Apabila kita tidak menyertakan potongan kode `{% csrf_token %}` pada elemen <form>, akan muncul Error 403 Forbidden dengan keterangan "CSRF verification failed. Request aborted." karena CSRF Tokennya tidak dapat ditemukan.Sehingga, user tidak dapat mengakses halaman HTMLnya


### ○ Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Tentu saja kita dapat membuat elemen <form> secara manual dengan memanfaatkan elemen <input> pada `.html`. Pertama, kita dapat mendefinisikan elemen <form> terlebih dahulu, kemudian di dalam tag <form> kita dapat mendefinisikan elemen <label> sebagai pendanda input dan <input> sebagai tempat user mengisikan data dengan text area, radio button, atau tipe lain. Input ini dapat disesuaikan keperluannya, setidaknya terdapat 22 tipe input. Tipe input yang digunakan pada tugas ini adalah text, password, dan submit untuk melakukan action yang telah didefinisikan pada elemen <form>.

Kemudian jika ingin tampilan form dapat lebih rapih, kita dapat emnggunakan elemen <table>. Kemudian, untuk mengisi data dari table tersebut kita dapat menggunakan elemen <tr> untuk mendefinisikan data di suatu row atau baris, kemudian di elemen tersebut kita definisikan lagi <td> atau table data yang ingin kita letakkan. Pada <td> inilah kita juga menggunakan elemen <input> sebagai text field area user memasukan suatu input untuk form. Berikut adalah potongan kode contoh form sederhana:

```html
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname">
</form>
```

### ○ Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

### ○ Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

 
 
 