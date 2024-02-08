from django.db import models
import datetime
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateField(default=datetime.date.today)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="todo")
    priority = models.CharField(max_length=20, default="low")
    assigned_users = models.ManyToManyField(User, related_name="assigned_tasks")