from .test_setup import TestSetup
from django.urls import reverse
from ..models import Task


class TestViews(TestSetup):

    def test_user_is_not_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {''}")
        resp = self.client.get(reverse("check_auth"))

        self.assertEqual(resp.status_code, 401)

    def test_user_is_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        resp = self.client.get(reverse("check_auth"))

        self.assertEqual(resp.status_code, 200)

    def test_user_can_create_task(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

        resp = self.client.post(self.tasks_url, self.dummy_task)

        self.assertEqual(resp.status_code, 201)

    def test_user_can_get_request_tasks(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        resp = self.client.get(reverse("tasks"))

        self.assertEqual(resp.status_code, 200)
        self.assertIn("title", resp.data[0])

    def test_user_can_logout(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

        resp = self.client.post(self.logout_url)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["message"], "logout successful")
