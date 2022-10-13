# Tugas 6 PBP Gasal 2023
### Annisa Az Zahra - 2106701242 - PBP A

## Link App Heroku
Nama App : app-annisa-tugas-2

[🌸 App Page](https://app-annisa-tugas-2.herokuapp.com/todolist/)

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asynchronus programming adalah pemrograman yang akan memungkinkan suatu proses dieksekusi secara independen tanpa terikat dengan proses lain, dengan komunikasi asynchronus user dapat berinteraksi (menjalankan beberapa proses atau event secara serentak) dengan webpage tanpa harus menunggu response dari servernya. Contohnya pada chat, email, dan notifikasi. Komunikasi servernya akan terjadi di belakang layar dengan memanfaatkan Ajax. Sedangkan synchronous programming adalah pemrograman yang menjalankan suatu proses dijalankan satu per satu, sehingga user harus menunggu hingga webpage memberikan response baru dapat melakukan event lain. 

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma Event-Driven Programming adalah suatu paradigma pemrograman dimana suatu program akan dieksekusi berdasarkan event yang dilakukan oleh user (seperti mouseclick, keyboard, dan lainnya). Salah satu contoh penerapannya pada tugas ini adalah ketika user ingin membuat task baru. User akan melakukan event mouse click pada button submit untuk menambahkan task, kemudian dari trigger yang dilakukan oleh user itu, method pun akan dieksekusi.

## Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous programming pada AJAX adalah ketika request dari user tidak akan mengganggu serangkaian proses yang sedang dieksekusi di suatu webpage. Dengan memanfaatkan AJAX, halaman tidak akan ter-refresh setiap ada proses baru sehingga tidak memberhentikan semua proses yang sedang diekseskusi. AJAX yang diteapkan akan membaca setiap request user dan memberikan response yang diproses secara asynchronous di server. 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
### AJAX GET
1. Membuat view baru yang mengembalikan seluruh data task dalam bentuk JSON pada `views.py`
```python
@login_required(login_url='/todolist/login/')
def show_json(request):
    data = ToDoList.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

2. Membuat path `/todolist/json` yang mengarah ke view yang baru di `urls.py`
```python
...
path('json/',show_json,name="show_json"),
...
```

3. Melakukan pengambilan task menggunakan AJAX GET.
```javascript
$(document).ready(function() {
    $.get("/todolist/json/", function(todolist) {
        console.log(todolist);
        for (i = 0; i < todolist.length; i++){
            $(".card-grid").append(
            `      
            ...
            `)
        }
});
```

### AJAX POST
Sebelumnya import Bootstrap CSS dan AJAX Jquery pada bagian `<head>`
```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
```

1. Membuat button Add Task yang membuka sebuah modal dengan form untuk menambahkan task pada `todolist.html`
```html
<!-- Button -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
    ✚ Tambah Task Baru
</button>

<!-- Modal -->
<div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true"> 
...
</div>
```

2. Membuat view baru untuk menambahkan task baru ke dalam database.
```python
@csrf_exempt
def create_todolist_ajax(request):
    ...
    return JsonResponse(result)
```

3. Membuat path `/todolist/add` yang mengarah ke view yang baru dibuat.
```python
...
path('add/', create_todolist_ajax, name='create_todolist_ajax'),
...
```

4. Menghubungkan form yang telah dibuat di dalam modal kamu ke path `/todolist/add` dan melakukan pembuatan task menggunakan AJAX POST. ID dari button akan diambil dan data yang masuk akan di-append pada card grid yang idnya telah disesuaikan
```javascript
$("#submit").click(function(){
    $.post("/todolist/add/", {
        title : $('#title').val(),
        description: $('#description').val()},
        function (result) {
            $(".card-grid").append(
            `      
            ...
            `)
            $('#title').val(''),
            $('#description').val('')
        }
    )
})
```
