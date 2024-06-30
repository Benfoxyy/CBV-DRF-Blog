from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = "blog"

urlpatterns = [
    path("comments/<int:pk>/", views.CommentViewSet.as_view(), name="comments"),
]

router = DefaultRouter()
router.register("posts", views.BlogPosts, basename="posts")
router.register("category", views.CategoryViewSet, basename="category")
urlpatterns += router.urls
