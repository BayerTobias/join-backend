from rest_framework import serializers
from join.models import Task, Category
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    # due_date = serializers.DateField(source="dueDate")

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["author", "assigned_users"]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username"]
