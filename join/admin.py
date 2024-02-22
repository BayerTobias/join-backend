from django.contrib import admin
from .models import Task

# Register your models here.


class Task_Admin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "priority")
    list_filter = ("priority",)
    list_display_links = ("id", "title")


admin.site.register(Task, Task_Admin)
