from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response
from .serializers.common import SignInSerializer
from .serializers.common import ContributorSerializer
from .serializers.token import TokenSerializer

from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

# Create your views here.

# * Path: /users

class UsersListView(APIView):
    def get(self, request):
        users = User.objects.all() 
        serializer = ContributorSerializer(users, many=True)
        return Response(serializer.data)
    


class SignInView(APIView):
    def post(self, request): 
        serialized_user = SignInSerializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)

        user = authenticate(
            username=serialized_user.validated_data['username'],
            password=serialized_user.validated_data['password']
        )
        
        if not user:
            return Response(
                {'error': 'Invalid credentials'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        }, status=status.HTTP_200_OK)

class UserUpdateView(APIView):
    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContributorSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

