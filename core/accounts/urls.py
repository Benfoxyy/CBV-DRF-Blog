from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [
    # user registration
    path(
        "registration/", views.RegistrationApi.as_view(), name="registration"
    ),
    # my profile
    path("user/me/", views.GetMe.as_view(), name="me"),
    # get other users profile
    path("user/<str:username>/", views.GetUser.as_view(), name="get-user"),
    # create jwt token
    path(
        "jwt/create/",
        views.CustomTokenObtainPairView.as_view(),
        name="create",
    ),
    # refresh jwt token
    path("jwt/refresh/", TokenRefreshView.as_view(), name="refresh"),
    # validate jwt token
    path("jwt/valide/", TokenVerifyView.as_view(), name="valid"),
    # check verification code
    path("verify/<str:token>", views.Verification.as_view(), name="verify"),
    # Resend verification token
    path("resend/", views.ResendToken.as_view(), name="resend"),
    # change password
    path(
        "password/change/", views.ChangePassword.as_view(), name="change-pass"
    ),
    # reset password
    path("password/reset/", views.ResetPassword.as_view(), name="reset-pass"),
    # reset password confirmation email
    path(
        "password/reset/conf/<str:token>",
        views.ResetPasswordConf.as_view(),
        name="reset-pass-conf",
    ),
]
