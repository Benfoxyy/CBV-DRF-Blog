from rest_framework.test import APIClient
import pytest
from django.urls import reverse
from datetime import datetime
from accounts.models import User


# Create a user for use it in tests
@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="example@example.com",
        username="example",
        password="passpass",
        is_verified=True,
    )
    return user


# Blog tests
@pytest.mark.django_db
class TestPostApi:
    client = APIClient()

    def test_get_post_response_200(self):
        url = reverse("blog:post-list")
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401(self):
        url = reverse("blog:post-list")
        data = {"title": "test", "content": "test", "created_date": datetime.now()}
        response = self.client.post(url, data)
        assert response.status_code == 401

    def test_post_response(self, common_user):
        data = {
            "pk": 1,
            "title": "test",
            "content": "test",
            "created_date": datetime.now(),
        }
        post_list_url = reverse("blog:post-list")
        single_post_url = reverse("blog:post-detail", kwargs={"pk": data.get("pk")})
        user = common_user
        self.client.force_login(user=user)
        post_list_response = self.client.post(post_list_url, data)
        single_post_response = self.client.get(single_post_url)
        data.update({"title": "put"})
        single_post_put_response = self.client.put(single_post_url, data)
        single_post_patch_response = self.client.patch(
            single_post_url, data={"title": "patch"}
        )
        single_post_delete_response = self.client.delete(single_post_url)
        assert post_list_response.status_code == 201
        assert single_post_response.status_code == 200
        assert single_post_put_response.status_code == 200
        assert single_post_patch_response.status_code == 200
        assert single_post_delete_response.status_code == 204

    def test_create_invalid_post_response_400(self, common_user):
        url = reverse("blog:post-list")
        data = {}
        user = common_user
        self.client.force_login(user=user)
        response = self.client.post(url, data)
        assert response.status_code == 400
