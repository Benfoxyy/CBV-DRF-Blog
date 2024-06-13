from rest_framework.routers import DefaultRouter
from . import views

app_name = "blog"

router = DefaultRouter()
router.register("posts", views.BlogPosts,basename='blog')
router.register("category", views.CategoryViewSet,basename='category')
urlpatterns = router.urls
