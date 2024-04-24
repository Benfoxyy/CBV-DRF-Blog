from django.urls import path
from . import views

urlpatterns = [
    path('post/',views.PostApi),
    path('detail/<int:id>/',views.DetailApi)
]
