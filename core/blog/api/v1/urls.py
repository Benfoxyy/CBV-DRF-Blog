from django.urls import path
from . import views

urlpatterns = [
    path('post/',views.PostApi),
    path('post/<int:id>/',views.PostDetailApi),
]
