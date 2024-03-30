from django.shortcuts import render, get_object_or_404

from .models import Task, Category, CustomUser, Contact
from join_backend.serializers import (
    TaskSerializer,
    CategorySerializer,
    UserListSerializer,
    ContactSerializer,
    UserSerializer,
)

from rest_framework.serializers import ValidationError

from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .functions import testFunction


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        contacts = ContactSerializer(user.contacts.all(), many=True).data

        user_data = UserSerializer(user).data

        return Response(
            {
                "token": token.key,
                "user": user_data,
                "contacts": contacts,
            }
        )


class TaskView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            category_id = request.data.get("category")
            category = get_object_or_404(Category, pk=category_id)

            assigned_user_ids = request.data.get("assigned_users", [])
            assigned_users = CustomUser.objects.filter(pk__in=assigned_user_ids)

            task = serializer.save(
                author=request.user,
                assigned_users=assigned_users,
                category=category,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleTaskView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        serializer = TaskSerializer(instance=task, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save(
                author=request.user,
            )

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        task.delete()

        return Response(
            {"message": "User created successfully"}, status=status.HTTP_201_CREATED
        )


class CategorysView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserView(APIView):

    def post(self, request):
        username = request.data.get("username")
        first_name = request.data.get("firstname")
        last_name = request.data.get("lastname")
        email = request.data.get("email")
        password = request.data.get("password")
        initials = request.data.get("initials")
        color = request.data.get("color")

        if CustomUser.objects.filter(username=username).exists():
            return Response(
                {"message": "This username already exists"},
                status=status.HTTP_409_CONFLICT,
            )

        if CustomUser.objects.filter(email=email).exists():
            return Response(
                {"message": "This email already exists"},
                status=status.HTTP_409_CONFLICT,
            )

        user = CustomUser.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            initials=initials,
            color=color,
        )

        return Response(
            {"message": "User created successfully"}, status=status.HTTP_201_CREATED
        )


class DeleteUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request):

        user = request.user
        user.delete()

        return Response(
            {"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class UserListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        users = CustomUser.objects.all()

        serializer = UserListSerializer(users, many=True)

        return Response(serializer.data)


class ContactView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, contact_id):
        contact = get_object_or_404(Contact, pk=contact_id)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, contact_id):
        contact = get_object_or_404(Contact, pk=contact_id)
        serializer = ContactSerializer(instance=contact, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
