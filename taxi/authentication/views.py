from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.serializers import UserSerializer, LogInSerializer


class SignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer


class LogInView(TokenObtainPairView):
    serializer_class = LogInSerializer
