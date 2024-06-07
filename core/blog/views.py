from rest_framework.viewsets import ModelViewSet
from blog.models import Post, Category
from .serializers import BlogSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .paginations import CustomPagination


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogPosts(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category"]
    search_fields = ["author__username", "title"]
    ordering_fields = ["created_date"]
    pagination_class = CustomPagination


# class FollowerPosts()
