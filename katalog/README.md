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
  
  
  
  
  
  
  
  > Source: Rekaman kelas PBP A - Selasa, 14 September 2022 (https://drive.google.com/drive/folders/12NE5Dr2ujyVZYjI7RmaJIB9VaMh_mRFj)
