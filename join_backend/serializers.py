from rest_framework import serializers
from join.models import Task, Category, CustomUser, Contact


"""
Serializer for Task model.
"""


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["author", "assigned_users"]


"""
 Serializer for Category model.
"""


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


"""
Serializer for list view of CustomUser model.
"""


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["id", "initials", "color", "first_name", "last_name"]


"""
Serializer for detail view of CustomUser model.
"""


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "initials",
            "color",
            "first_name",
            "last_name",
            "email",
        ]


"""
Serializer for Contact model.
"""


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ["id", "name", "email", "phone", "initials", "color"]
