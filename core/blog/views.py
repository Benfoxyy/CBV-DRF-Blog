from rest_framework.viewsets import ModelViewSet
from blog.models import Post, Category
from .serializers import BlogSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogPosts(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category"]
    search_fields = ["author__username", "title"]
    ordering_fields = ["created_date"]


# class FollowerPosts()
