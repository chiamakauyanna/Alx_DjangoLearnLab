from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.views import APIView

User = get_user_model()

# Create your views here.
class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer
  
class LoginView(APIView):
  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      token, created = Token.objects.get_or_create(user=user)
      return Response({'token': token.key})
    return Response({'error': 'Invalid credentials'}, status=400)
  

class ProfileView(generics.RetrieveUpdateAPIView):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = UserSerializer
  
  def get_object(self):
    return self.request.user