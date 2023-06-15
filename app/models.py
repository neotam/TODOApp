from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=32, null=False, unique=True)
    first_name = models.CharField(max_length=32, null=False, unique=False)
    last_name = models.CharField(max_length=32, null=False, unique=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=64)


class Category(models.Model):
    name = models.CharField(max_length=32)
    desc = models.TextField()


class Task(models.Model):
    task_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    due_time = models.TimeField(null=True)
    isfin = models.BooleanField(default=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


