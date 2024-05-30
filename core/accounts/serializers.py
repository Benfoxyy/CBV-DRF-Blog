from rest_framework import serializers
from .models import Profile, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.shortcuts import get_object_or_404


class RegistrationSerializer(serializers.ModelSerializer):
    pass_conf = serializers.CharField()

    class Meta:
        model = User
        fields = ["email", "username", "password", "pass_conf"]

    def validate(self, attrs):
        try:
            validate_password(attrs.get("password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(list(e.messages))
        if attrs.get("password") != attrs.get("pass_conf"):
            raise serializers.ValidationError(
                {"password": "passwords does not match"}
            )
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("pass_conf", None)
        return User.objects.create_user(**validated_data)


class ResendTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        user_obj = get_object_or_404(User, email=attrs.get("email"))
        attrs["user"] = user_obj
        if user_obj.is_verified:
            raise serializers.ValidationError(
                {"user": "user is already verified"}
            )
        return super().validate(attrs)


class GetMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "user", "avatar", "bio"]
        read_only_fields = ["user"]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        if not self.user.is_verified:
            raise serializers.ValidationError(
                {"detail": "User is not verifide yet"}
            )
        data.update({"email": self.user.email})
        data.update({"username": self.user.username})
        data.update({"id": self.user.id})
        return data


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=8, required=True)
    new_pass = serializers.CharField(min_length=8, required=True)

    def validate(self, attrs):
        try:
            validate_password(attrs.get("new_pass"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(list(e.messages))

        return super().validate(attrs)


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        user_obj = get_object_or_404(User, email=attrs.get("email"))
        attrs["user"] = user_obj
        return super().validate(attrs)


class ResetPasswordConfSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    new_password_conf = serializers.CharField(required=True)

    def validate(self, attrs):
        try:
            validate_password(attrs.get("new_password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(list(e.messages))
        if attrs.get("new_password") != attrs.get("new_password_conf"):
            raise serializers.ValidationError(
                {"error": "password does not match"}
            )
        return super().validate(attrs)


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "bio",
            "avatar",
        ]
