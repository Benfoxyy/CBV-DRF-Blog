from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("blog", views.BlogPosts)
urlpatterns = router.urls
