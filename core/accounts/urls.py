from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView

urlpatterns = [
    # my profile
    path('users/me/',views.GetMe.as_view(),name = 'me'),
    # create jwt token
    path('jwt/create/',views.CustomTokenObtainPairView.as_view(),name = 'create'),
    # refresh jwt token
    path('jwt/refresh/',TokenRefreshView.as_view(),name = 'refresh'),
    # validate jwt token
    path('jwt/valide/',TokenVerifyView.as_view(),name = 'valid'),
]
