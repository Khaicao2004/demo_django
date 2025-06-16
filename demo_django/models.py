from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Books(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
