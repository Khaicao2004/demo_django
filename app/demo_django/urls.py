from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index_users, name='users.index'),
    path('users/', views.index_users, name='users.index'),
    path('users/create/', views.create_users, name='users.create'),
    path('users/store/', views.store_users, name='users.store'),
    path('users/edit/<str:id>', views.edit_users, name='users.edit'),
    path('users/update/<str:id>', views.update_users, name='users.update'),
    path('users/delete/<str:id>', views.delete_users, name='users.delete'),
    path('books/', views.index_books, name='books.index'),
    path("__reload__/", include("django_browser_reload.urls")),
]
