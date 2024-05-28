from .serializers import GetMeSerializer,CustomTokenObtainPairSerializer
from rest_framework import generics
from .models import Profile
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView


class GetMe(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = GetMeSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset,user=self.request.user)
        return obj
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer