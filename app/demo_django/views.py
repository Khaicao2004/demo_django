from django.shortcuts import render, redirect, get_object_or_404
from .models import Users

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
        password = request.POST.get('password')
        Users.objects.create(name=name, email=email, password=password)
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
        Users.objects.get(id=id).update(name=name,email=email)
    return redirect('users.index')

def delete_users(request, id):
    if request.method == 'POST':
        Users.objects.filter(id=id).delete()
        return redirect('users.index')