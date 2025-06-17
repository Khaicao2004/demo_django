from django.shortcuts import render, redirect, get_object_or_404
from .models import Users
from django.contrib import messages


# Create your views here.
def index_users(request):
    users = Users.objects.all()
    return render(request, 'users/index.html', {
        'users': users
    })
def create_users(request):
    return render(request, 'users/create.html')

def store_users(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        Users.objects.create(name=name, email=email, address=address, phone=phone)
        messages.success(request, 'Lưu bản ghi thành công')
    else:
        messages.error(request, 'Lưu bản ghi thất bại')
    return redirect('users.index')

def edit_users(request, id): 
    user = Users.objects.get(id=id)
    return render(request, 'users/edit.html', {
        'user': user
    })

def update_users(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        Users.objects.filter(id=id).update(name=name,email=email, address=address, phone=phone)
        messages.success(request, 'Cập nhật bản ghi thành công')
    else:
        messages.error(request, 'Cập nhật bản ghi thất bại')
    return redirect('users.index')

def delete_users(request, id):
    if request.method == 'POST':
        Users.objects.get(id=id).delete()
        messages.success(request, 'Xoá bản ghi thành công')
    else:
        messages.error(request, 'Xoá bản ghi thất bại')
    return redirect('users.index')