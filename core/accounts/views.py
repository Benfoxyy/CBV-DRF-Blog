from .serializers import (
    GetMeSerializer,
    CustomTokenObtainPairSerializer,
    RegistrationSerializer,
    ResendTokenSerializer,
    ChangePasswordSerializer,
    ResetPasswordSerializer,
    ResetPasswordConfSerializer,
    GetUserSerializer,
)
from rest_framework import generics
from .models import Profile, User
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView
from mail_templated import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import EmailThread
from rest_framework.views import APIView
import jwt
from jwt.exceptions import (
    ExpiredSignatureError,
    InvalidSignatureError,
    DecodeError,
)
from rest_framework.response import Response
from decouple import config
from rest_framework import status


# registraion api view
class RegistrationApi(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        serializer.save()
        user_obj = get_object_or_404(User, email=email)
        token = self.get_tokens_for_user(user=user_obj)
        email_obj = EmailMessage(
            "email/verify.tpl",
            {"token": token},
            "benxfoxy@gmail.com",
            to=[email],
        )
        EmailThread(email_obj).start()
        return Response({"success": "email successfully sent"})

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


# Resend token view that send again verification email
class ResendToken(generics.GenericAPIView):
    serializer_class = ResendTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = ResendTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        user_obj = serializer.validated_data["user"]
        token = self.get_tokens_for_user(user=user_obj)
        email_obj = EmailMessage(
            "email/verify.tpl",
            {"token": token},
            "benxfoxy@gmail.com",
            to=[email],
        )
        EmailThread(email_obj).start()
        return Response({"success": "email successfully sent"})

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    
# see other users profile
class GetUser(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = GetUserSerializer
    lookup_field = "username"

    def get(self, request, username, *args, **kwargs):
        queryset = self.get_queryset().get(user__username=username,user__is_verified=True)
        serializer = GetUserSerializer(queryset)
        return Response(serializer.data)


# See your profile
class GetMe(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = GetMeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# Check the verification email that sended before to user
class Verification(APIView):
    def get(self, request, token, *args, **kwargs):
        try:
            info = jwt.decode(
                token, config("SECRET_KEY"), algorithms=["HS256"]
            )
        except ExpiredSignatureError:
            return Response(
                {"error": "token has been expired"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except InvalidSignatureError:
            return Response(
                {"error": "token has been wrong"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except DecodeError:
            return Response(
                {"error": "token has been used once"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user_obj = User.objects.get(pk=info.get("user_id"))
        if user_obj.is_verified:
            return Response({"user": "user is already verified"})
        user_obj.is_verified = True
        user_obj.save()
        return Response({"success": "user successfully verified"})


# Changing password view
class ChangePassword(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not self.object.check_password(serializer.data.get("password")):
            return Response(
                {"error": "Invalid password"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        self.object.set_password(serializer.data.get("new_pass"))
        self.object.save()
        return Response(
            {"success": "password changed successfully"},
            status=status.HTTP_201_CREATED,
        )


# Reset password from email
class ResetPassword(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.validated_data["user"]
        if not user_obj.is_verified:
            return Response(
                {"error": "user is not verified"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        token = self.get_tokens_for_user(user=user_obj)
        email_obj = EmailMessage(
            "email/resetverify.tpl",
            {"token": token},
            "benxfoxy@gmail.com",
            to=[user_obj.email],
        )
        EmailThread(email_obj).start()
        return Response({"success": "reset password email sent successfully"})

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


# Password reset confirmation email
class ResetPasswordConf(generics.GenericAPIView):
    serializer_class = ResetPasswordConfSerializer

    def get(self, request, token, *args, **kwargs):
        try:
            info = jwt.decode(
                token, config("SECRET_KEY"), algorithms=["HS256"]
            )
        except ExpiredSignatureError:
            return Response(
                {"error": "token has been expired"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except InvalidSignatureError:
            return Response(
                {"error": "token has been wrong"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except DecodeError:
            return Response(
                {"error": "token has been used once"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        global user_obj
        user_obj = User.objects.get(pk=info.get("user_id"))

        return Response({user_obj.email})

    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordConfSerializer(data=request.data)
        self.object = user_obj
        serializer.is_valid(raise_exception=True)
        self.object.set_password(serializer.validated_data["new_password"])
        self.object.save()
        return Response(
            {"success": "password successfully reset and commited new one"},
            status=status.HTTP_201_CREATED,
        )
