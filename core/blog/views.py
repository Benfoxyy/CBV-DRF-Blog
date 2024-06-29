from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .paginations import CustomPagination
<<<<<<< Updated upstream
from .serializers import BlogSerializer, CategorySerializer
from blog.models import Post, Category
=======
from .serializers import BlogSerializer, CategorySerializer, CommentSerializer
from blog.models import Post, Category, Comments


@method_decorator(cache_page(60 * 2), name="dispatch")
class CommentViewSet(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comments.objects.all()
        # param = self.request.query_params.get('pk')
        queryset = queryset.filter(post__id=self.kwargs["pk"])
        return queryset
>>>>>>> Stashed changes


@method_decorator(cache_page(60 * 2), name="dispatch")
class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


@method_decorator(cache_page(60 * 2), name="dispatch")
class BlogPosts(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category"]
    search_fields = ["author__username", "title"]
    ordering_fields = ["created_date"]
    pagination_class = CustomPagination
