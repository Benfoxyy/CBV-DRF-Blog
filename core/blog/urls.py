from django.urls import path
from . import views
from django.urls import include

app_name = 'blog'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.SingleView.as_view(),name='single'),
    path('add_form/',views.CreatePost.as_view(),name = 'pform'),
    path('api/v1/',include('blog.api.v1.urls')),

]
