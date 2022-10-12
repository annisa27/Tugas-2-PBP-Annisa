from asyncio.base_tasks import _task_print_stack
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpRequest
from django.core import serializers

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.models import ToDoList


from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='login/')
def show_todolist(request):
    todolist_data = ToDoList.objects.filter(user=request.user)
    context = {
    'todo': todolist_data,
    'username' : request.user,
    }
    return render(request, "todolist.html",context=context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {
    }
    return render(request, 'login.html', context)

@login_required(login_url='login/')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='login/')
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title != "" and description != "":
            ToDoList.objects.create(title=title, description=description, date=datetime.date.today(), user=request.user)
            info_message = 'Task "{title}" telah berhasil disimpan!'.format(title= title)
            messages.info(request, info_message)
            return HttpResponseRedirect(reverse("todolist:show_todolist")) 
        
        messages.info(request, 'Judul atau Deskripsi belum diisi!')

    return render(request, "create.html")


@login_required(login_url='/todolist/login/')
def task_status(request, key):
    task = ToDoList.objects.get(
        user = request.user,
        pk = key
    )
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def delete_task(request, key):
    task = ToDoList.objects.get(
        user = request.user,
        pk = key
    )
    task.delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def show_json(request):
    data = ToDoList.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    tasklist = ToDoList.objects.filter(user=request.user)
    context = {
        'tasks' : tasklist,
        'username' : request.user,
    }
    return render(request, "todolist.html", context)

@csrf_exempt
def create_todolist_ajax(request):
    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        task = ToDoList.objects.create(title=title, description=description, date=datetime.date.today(), user=request.user)
        
        result = {
            'fields':{
                'title':task.title,
                'description':task.description,
                'date':task.date,
            },
            'pk':task.pk
        }
        print(result)

        return JsonResponse(result)