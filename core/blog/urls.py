from rest_framework.routers import DefaultRouter
from . import views

app_name = "blog"

router = DefaultRouter()
router.register("blog", views.BlogPosts)
urlpatterns = router.urls
