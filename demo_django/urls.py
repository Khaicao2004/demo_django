from django.urls import path, include
from .views import index_users,create_users, store_users, edit_users, update_users, delete_users
urlpatterns = [
    path('', index_users, name='users.index'),
    path('create/', create_users, name='users.create'),
    path('store/', store_users, name='users.store'),
    path('edit/<str:id>', edit_users, name='users.edit'),
    path('update/<str:id>', update_users, name='users.update'),
    path('delete/<str:id>', delete_users, name='users.delete'),
    path("__reload__/", include("django_browser_reload.urls")),
]
