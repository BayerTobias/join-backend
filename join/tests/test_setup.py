from rest_framework.test import APITestCase
from django.urls import reverse

from ..models import Category, Task


class TestSetup(APITestCase):

    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")
        self.tasks_url = reverse("tasks")

        self.user_data = {
            "username": "username",
            "firstname": "firstname",
            "lastname": "lastname",
            "email": "email",
            "password": "password",
            "initials": "initials",
            "color": "color",
        }

        self.categorys = Category.objects.create(name="dummy 1", color="#000000")
        self.dummy_task = {
            "title": "dummy task",
            "description": "dummy description",
            "created_at": "2024-03-03",
            "due_date": "2024-05-06",
            "author": 1,
            "status": "todo",
            "priority": "high",
            "assigned_users": [1],
            "category": 1,
            "subtasks": [],
        }

        # Register
        self.client.post(self.register_url, self.user_data)
        # Login
        login_resp = self.client.post(self.login_url, self.user_data)
        # set Authorization
        self.token = login_resp.data.get("token")
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        # create Dummy Task
        self.client.post(self.tasks_url, self.dummy_task)
        tasks = Task.objects.count()
        print("tasks : ", tasks)
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
