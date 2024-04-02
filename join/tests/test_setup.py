from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetup(APITestCase):

    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")

        self.user_data = {
            "username": "username",
            "firstname": "firstname",
            "lastname": "lastname",
            "email": "email",
            "password": "password",
            "initials": "initials",
            "color": "color",
        }

        self.dummy_task = {}

        # Register
        self.client.post(self.register_url, self.user_data)
        # Login
        login_resp = self.client.post(self.login_url, self.user_data)
        self.token = login_resp.data.get("token")
        # set Authorization

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
