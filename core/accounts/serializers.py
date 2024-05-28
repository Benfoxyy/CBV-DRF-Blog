from rest_framework import serializers
from .models import Profile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class GetMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','user','first_name','last_name','avatar','bio']
        read_only_fields = ['user']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({'user': self.user.email})
        data.update({'id': self.user.id})
        # and everything else you want to send in the response
        return data