from django.db import models
from accounts.models import Profile


class Comments(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey("Post", on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.post} - {self.content}"


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True, null=True
    )
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:15] + "..."


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
