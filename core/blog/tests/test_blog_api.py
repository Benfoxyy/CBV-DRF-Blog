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
        url = reverse("blog:posts-list")
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401(self):
        url = reverse("blog:posts-list")
        post_data = {"title": "test", "content": "test", "created_date": datetime.now()}
        response = self.client.post(url, post_data)
        assert response.status_code == 401

    def test_post_response(self, common_user):
        post_data = {
            "pk": 1,
            "title": "test",
            "content": "test",
            "created_date": datetime.now(),
        }
        comment_data = {
            "content": "nice bro"
        }
        post_list_url = reverse("blog:posts-list")
        single_post_url = reverse("blog:posts-detail", kwargs={"pk": post_data.get("pk")})
        comments_url = reverse("blog:comments", kwargs={"pk": post_data.get("pk")})
        user = common_user
        self.client.force_login(user=user)
        post_list_response = self.client.post(post_list_url, post_data)
        single_post_response = self.client.get(single_post_url)
        single_post_put_response = self.client.put(single_post_url, post_data.update({"title": "put"}))
        single_post_patch_response = self.client.patch(
            single_post_url, post_data.update({"title": "patch"})
        )
        comments_post_response = self.client.post(comments_url, comment_data)
        comments_get_response = self.client.get(comments_url)
        comments_put_response = self.client.put(comments_url, comment_data.update({"content": "put"}))
        comments_patch_response = self.client.patch(comments_url, comment_data.update({"content": "patch"}))
        single_post_delete_response = self.client.delete(single_post_url)
        assert post_list_response.status_code == 201
        assert single_post_response.status_code == 200
        assert single_post_put_response.status_code == 200
        assert single_post_patch_response.status_code == 200
        assert comments_get_response.status_code == 200
        assert comments_post_response.status_code == 201
        assert comments_put_response.status_code == 200
        assert comments_patch_response.status_code == 200
        assert single_post_delete_response.status_code == 204


